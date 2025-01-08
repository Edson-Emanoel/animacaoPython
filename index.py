import flet as ft;
import asyncio;

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    async def animate(e = None): 
        while True:
            img.offset.y = -0.3
            img.scale.scale = 1.2
            img.update()
            await asyncio.sleep(4)
            
            img.offset.y = 0
            img.scale.scale = 1
            img.update()
            await asyncio.sleep(4)

    img = ft.Image(
        src = 'https://gmedia.playstation.com/is/image/SIEPDC/dualsense-edge-listing-thumb-01-en-23aug22?$facebook$',
        width  = 450,
        height = 450,
        scale  = ft.Scale(scale = 1),
        offset = ft.Offset(x=0, y=0),
        animate_offset = ft.Animation(duration=4000, curve=ft.AnimationCurve.EASE),
        animate_scale  = ft.Animation(duration=4000, curve=ft.AnimationCurve.EASE),
        animate_opacity= ft.Animation(duration=4000, curve=ft.AnimationCurve.EASE)
    )

    page.add(img)
    
    page.run_task(animate)

if __name__ == '__main__':
    ft.app(target = main)