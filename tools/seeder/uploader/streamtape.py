import os
import httpx
import asyncio
import dotenv

dotenv.load_dotenv()


STREAMTAPE_LOGIN = os.getenv("STREAMTAPE_LOGIN")
STREAMTAPE_KEY = os.getenv("STREAMTAPE_KEY")
STREAMTAPE_PARENT_FOLDER_ID = "eAOuUTmAPAE"


async def create_folder(name: str) -> str:
    """
    Create a new folder in Streamtape using the Streamtape API.

    Args:
    name (str): The name of the folder to be created.

    Returns:
    str: The ID of the newly created folder, or the ID of the parent folder if folder creation fails.

    Note:
    This function requires the following constants to be defined: LOGIN, KEY, and PARENT_FOLDER_ID.
    """
    async with httpx.AsyncClient() as client:
        url = "https://api.streamtape.com/file/createfolder"
        params = {
            "login": STREAMTAPE_LOGIN,
            "key": STREAMTAPE_KEY,
            "name": name,
            "pid": STREAMTAPE_PARENT_FOLDER_ID,
        }
        response = await client.get(url, params=params)

        if response.status_code == 200:
            folder_id_data = response.json()
            if result := folder_id_data["result"]:
                print(f"New folder created: {folder_id_data}")
                return result["folderid"]
            print("unable to create folder")
            return STREAMTAPE_PARENT_FOLDER_ID
        print(f"Error creating folder: {response.text}")
        return STREAMTAPE_PARENT_FOLDER_ID


async def get_upload_url(folder_id: str) -> str:
    async with httpx.AsyncClient() as client:
        url = "https://api.streamtape.com/file/ul"
        params = {"login": STREAMTAPE_LOGIN, "key": STREAMTAPE_KEY, "folder": folder_id}
        response = await client.get(url, params=params)
        if response.status_code == 200:
            return response.json()["result"]["url"]


async def upload(upload_url: str, file_path: str) -> bool:
    async with httpx.AsyncClient() as client:
        print("Uploading file...")
        response = await client.post(upload_url, files={"file1": open(file_path, "rb")})
        if response.status_code == 200:
            print("File uploaded successfully!")
            return response.json()["result"]["url"]
            # return response.json()["result"]["id"]
        print("Error uploading file:", response.json())


# # Examples :
# async def main():
#     folder_id = await create_folder(name="Death note")
#     print("Created folder id:", folder_id)
#     upload_url = await get_upload_url(folder_id)
#     print("Upload url: ", upload_url)
#     uploaded_file_url = await upload(upload_url, file_path="death_note-01.mp4")
#     print("Uploaded file url:", uploaded_file_url)


# if __name__ == "__main__":
#     asyncio.run(main())
