class LoginLocators:
    LOGIN_BUTTON_TEXT = ('//android.widget.TextView[@text="Login"]', 'xpath')
    USERNAME_AREA = ('//*[@text="Email"]', 'xpath')
    PASSWORD_AREA = ('//*[@text="Password"]', 'xpath')
    LOGIN_BUTTON = ('//*[@content-desc="button-LOGIN"]', 'xpath')
    SUCCESS_MESSAGE = ('//*[@text="Success"]', 'xpath')
    PASSWORD_VALIDATION = ('//*[@text="Please enter at least 8 characters"]', 'xpath')
    USERNAME_VALIDATION = ('//*[@text="Please enter a valid email address"]', 'xpath')


class SignUpLocators:
    SIGNUP_BUTTON_TEXT = ('//android.widget.TextView[@text="Sign up"]', 'xpath')
    USERNAME_AREA = ('input-email', 'accessibility')
    PASSWORD_AREA = ('input-password', 'accessibility')
    CONFIRM_PASSWORD = ('input-repeat-password', 'accessibility')
    SIGNUP_BUTTON = ('//android.view.ViewGroup[@content-desc="button-SIGN UP"]/android.view.ViewGroup', 'xpath')
    SUCCESS_MESSAGE = ('android:id/alertTitle', 'id')
    CONFIRM_PASSWORD_VALIDATION = ('//android.widget.TextView[@text="Please enter the same password"]', 'xpath')
    PASSWORD_VALIDATION = ('//android.widget.TextView[@text="Please enter at least 8 characters"]', 'xpath')
    USERNAME_VALIDATION = ('//android.widget.TextView[@text="Please enter a valid email address"]', 'xpath')


class DragAndDropLocators:
    DRAG_AND_DROP_TEXT = ('//android.widget.TextView[@text="Drag"]', 'xpath')
    IMAGE_DISPLAY = ('android.widget.ImageView', 'class')


class SwipeLocators:
    SWIPE_TEXT = ('//android.widget.TextView[@text="Swipe"]', 'xpath')
