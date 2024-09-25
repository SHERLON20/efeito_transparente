import flet as ft 
def main (page:ft.Page):
    page.padding=0
    layout=ft.Container(
        image_src='https://images3.alphacoders.com/133/1332803.png',
        image_fit=ft.ImageFit.COVER,
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Container(
            bgcolor=ft.colors.with_opacity(0.1,ft.colors.WHITE),
            padding=ft.padding.symmetric(vertical=40,horizontal=70),
            border_radius=ft.border_radius.all(20),
            border=ft.Border(
              top=ft.BorderSide(width=5,color=ft.colors.WHITE30),
              right=ft.BorderSide(width=5,color=ft.colors.WHITE30),  
            ),
            blur=ft.Blur(sigma_x=7,sigma_y=6),
            content=ft.Text(
                value="@sherlon.py",
                color=ft.colors.WHITE,
                size=40,
            ),
    )
        )
    page.add(layout)
if __name__=="__main__":
    ft.app(target=main)