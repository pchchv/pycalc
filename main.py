from flet import ( app, Page, ElevatedButton, Row )


def main(page: Page):
    page.title = "Calculator"

    def button_click(e):
        pass

    button_row0 = Row(
        [
            ElevatedButton(text='C',  on_click=button_click),
            ElevatedButton(text='^',  on_click=button_click),
            ElevatedButton(text='%',  on_click=button_click),
            ElevatedButton(text='/',  on_click=button_click),
        ]
    )
    button_row1 = Row(
        [
            ElevatedButton(text='7',  on_click=button_click),
            ElevatedButton(text='8',  on_click=button_click),
            ElevatedButton(text='9',  on_click=button_click),
            ElevatedButton(text='*',  on_click=button_click),
        ]
    )
    button_row2 = Row(
        [
            ElevatedButton(text='4',  on_click=button_click),
            ElevatedButton(text='5',  on_click=button_click),
            ElevatedButton(text='6',  on_click=button_click),
            ElevatedButton(text='-',  on_click=button_click),
        ]
    )
    button_row3 = Row(
        [
            ElevatedButton(text='1',  on_click=button_click),
            ElevatedButton(text='2',  on_click=button_click),
            ElevatedButton(text='3',  on_click=button_click),
            ElevatedButton(text='+',  on_click=button_click),
        ]
    )
    button_row4 = Row(
        [
            ElevatedButton(text='0',  on_click=button_click),
            ElevatedButton(text='.',  on_click=button_click),
            ElevatedButton(text='=',  on_click=button_click),
        ]
    )


if __name__ == '__main__':
    app(target=main)
