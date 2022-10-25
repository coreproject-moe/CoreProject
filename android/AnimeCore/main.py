"""Example shows the recommended way of how to run Kivy with the Python built
in asyncio event loop as just another async coroutine.
"""
import asyncio
import anyio

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from Views.Login.login import LoginScreen

from Views.MainScreen.main_screen import MainScreen


class AsyncApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.manager_screens = ScreenManager()

    def build(self):
        return self.manager_screens

    async def load_screens(self):
        self.manager_screens.add_widget(MainScreen())
        self.manager_screens.add_widget(LoginScreen())

    async def app_func(self):
        """This will run both methods asynchronously and then block until they
        are finished
        """

        async with anyio.create_task_group() as task_group:
            self.task_group = task_group

            async def run_wrapper():
                # trio needs to be set so that it'll be used for the event loop
                await self.async_run()
                print("App done")
                self.task_group.cancel_scope.cancel()

            self.task_group.start_soon(run_wrapper)
            self.task_group.start_soon(self.load_screens)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(AsyncApp().app_func())
    loop.close()
