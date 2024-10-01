from flet import (app, Page)


def main(page: Page):
    page.title = "Calculator"


if __name__ == '__main__':
    app(target=main)
