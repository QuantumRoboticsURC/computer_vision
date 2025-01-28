import asyncio
import websockets
import cv2
import base64
import numpy as np




async def video_client():
    uri = "ws://192.168.0.59:9999"  # Replace with the server's IP and port
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to the server.")
            while True:
                try:
                    # Receive the frame data
                    frame_data = await websocket.recv()

                    # Decode the base64 frame
                    frame_buffer = base64.b64decode(frame_data)
                    frame_array = np.frombuffer(frame_buffer, dtype=np.uint8)

                    # Decode the image
                    frame = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)

                    # Display the frame
                    cv2.imshow("Video Stream", frame)

                    # Exit on 'q' key press
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        print("Exiting...")
                        break
                except websockets.exceptions.ConnectionClosed as e:
                    print(f"Connection closed: {e}")
                    break
                except Exception as e:
                    print(f"Error receiving frame: {e}")
                    break
    except Exception as e:
        print(f"Failed to connect to the server: {e}")
    finally:
        cv2.destroyAllWindows()
        print("Client stopped.")

# Run the client
asyncio.get_event_loop().run_until_complete(video_client())
