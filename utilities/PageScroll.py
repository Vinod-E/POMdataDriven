class PageScroll:
    def __init__(self, driver):
        """
        :param driver:
        """
        self.driver = driver
        self.window_scroll = ""

    def up(self, x_axis, y_axis):
        """
        For Up USE Positive Y-AXIS VALUE

        :param x_axis:
        :param y_axis:
        :return:
        """
        self.window_scroll = "window.scrollTo({},{});".format(x_axis, y_axis)
        self.driver.execute_script(self.window_scroll)

    def down(self, x_axis, y_axis):
        """
        For Down USE Negative Y-AXIS VALUE

        :param x_axis:
        :param y_axis:
        :return:
        """
        self.window_scroll = "window.scrollTo({},{});".format(x_axis, y_axis)
        self.driver.execute_script(self.window_scroll)

    def right(self, x_axis, y_axis):
        """
        For Right Scroll USE Positive X-AXIS VALUE

        :param x_axis:
        :param y_axis:
        :return:
        """
        self.window_scroll = "window.scrollTo({},{});".format(x_axis, y_axis)
        self.driver.execute_script(self.window_scroll)

    def left(self, x_axis, y_axis):
        """
        For Left Scroll USE Negative X-AXIS VALUE

        :param x_axis:
        :param y_axis:
        :return:
        """
        self.window_scroll = "window.scrollTo({},{});".format(x_axis, y_axis)
        self.driver.execute_script(self.window_scroll)
