__author__ = 'Nicki Hirakawa'


import pyglet


def get_window():
	return pyglet.window.Window()


def main():
	window = get_window()
	pyglet.app.run()


if __name__ == '__main__':
	main()
