#!/usr/bin/env python3
"""
Quick test script to check if the Railway chess server is working
"""

import asyncio
import websockets
import json
import sys

SERVER_URL = "wss://chess-game-server-production-c34a.up.railway.app"

async def test_server():
    print(f"🔍 בודק חיבור לשרת: {SERVER_URL}")
    
    try:
        # Try to connect
        print("⏳ מנסה להתחבר...")
        async with websockets.connect(SERVER_URL, timeout=10) as websocket:
            print("✅ חיבור הצליח!")
            
            # Send a test message
            test_message = {
                "type": "NEW_GAME",
                "player_name": "TestPlayer"
            }
            
            print(f"📤 שולח הודעת בדיקה: {test_message}")
            await websocket.send(json.dumps(test_message))
            
            # Wait for response
            print("⏳ מחכה לתגובה...")
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=5)
                print(f"✅ התקבלה תגובה: {response}")
                
                # Try to parse the response
                try:
                    parsed_response = json.loads(response)
                    print(f"📋 תגובה מפוענחת: {parsed_response}")
                except json.JSONDecodeError:
                    print(f"⚠️  התגובה לא בפורמט JSON: {response}")
                
                return True
                
            except asyncio.TimeoutError:
                print("⏰ timeout - השרת לא הגיב תוך 5 שניות")
                return False
                
    except websockets.exceptions.ConnectionClosed as e:
        print(f"❌ החיבור נסגר: {e}")
        return False
    except websockets.exceptions.InvalidURI as e:
        print(f"❌ URL לא תקין: {e}")
        return False
    except ConnectionRefusedError:
        print("❌ השרת סירב לחיבור")
        return False
    except OSError as e:
        print(f"❌ שגיאת רשת: {e}")
        return False
    except Exception as e:
        print(f"❌ שגיאה לא צפויה: {e}")
        return False

async def main():
    print("🎯 בודק שרת שחמט ב-Railway")
    print("="*50)
    
    success = await test_server()
    
    print("="*50)
    if success:
        print("🎉 השרת עובד תקין!")
        sys.exit(0)
    else:
        print("💥 השרת לא עובד או יש בעיה")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
