from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import*

Builder.load_file("main.kv")

class Home(Screen):
    pass
class Second(Screen):
    pass

class MyApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Home(name="home"))
        sm.add_widget(Second(name="second"))
        sm.current="home"
        return sm
    
    def function_add(self, num):
        screen = self.root.get_screen("home")
        affiche = screen.ids.affiche
        if num in ["+", "-", "*", "/"]:
            self.first_num = float(affiche.text)
            self.operator = num
            affiche.text = "0"
        elif num == "=":
            if not hasattr(self, "operator"):
                return
            second_num = float(affiche.text)
            if self.operator == "+":
                result = self.first_num + second_num
            elif self.operator == "-":
                result = self.first_num - second_num
            elif self.operator == "*":
                result = self.first_num * second_num
            elif self.operator == "/":
                if second_num == 0:
                    affiche.text = "Error"
                    return
                result = self.first_num / second_num
            affiche.text = str(result)
            del self.operator
        else:
            if affiche.text == "0":
                affiche.text = str(num)
            else:
                affiche.text += str(num)

MyApp().run()