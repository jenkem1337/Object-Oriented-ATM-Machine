from view.abstract.IViewComponent import IViewComponent


class LoginViewComponent(IViewComponent):
    def printView(self) -> None:
        print("""
                            ATM Giriş Ekranı
        
        Sırasıyla Hesap Numarınızı, Kart Numarasını ve Kart Şifresini Girin
        """)
        

        