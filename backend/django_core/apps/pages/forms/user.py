from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Email / Username:",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "sora_amamiya@coreproject.moe / soraamamiya#0001",
                "class": "h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]",
            }
        ),
        help_text="we’ll send you a verification email, so please ensure it’s active",
    )

    password = forms.CharField(
        label="Password:",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "enter your existing password",
                "class": "h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
            }
        ),
    )


class FirstRegisterForm(forms.Form):
    email = forms.EmailField(
        label="Email:",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "sora_amamiya@coreproject.moe",
                "class": "h-12 w-full rounded-xl border-[0.4vw] bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
            }
        ),
        help_text="Please enter a valid email address",
    )
    password = forms.CharField(
        label="Password:",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "enter your existing password",
                "class": "h-12 w-full rounded-xl border-[0.4vw] bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
                "_": """
                    on keyup
                        set global password to my.value
                        js(password)
                            try{
                                return window.get_password_strength(password).score;
                            }catch (e){
                                console.log("Silenced errors")
                                return null
                            }
                        end
                        send hyperscript:password_strength(strength:it) to <password-strength/>
                """,
            }
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password:",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "re-enter your password",
                "class": "h-12 w-full rounded-xl border-[0.4vw] bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
                "_": """
                    on keyup
                        if my.value.length === 0
                            add .invisible to next <span/>

                        else
                            if my.value === password
                                add .invisible to next <span/>
                            else
                                remove .invisible from next <span/>
                            end
                        end
                """,
            }
        ),
        help_text="Please make sure you enter the same password in both fields",
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("`password` and `confirm_password` does not match")


class SecondRegisterForm(forms.Form):
    username = forms.CharField(
        label="Username:",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "choose any username",
                "class": "h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]",
            }
        ),
        help_text="you can change username in your user settings later, so go bonkers!",
    )

    otp = forms.CharField(
        label="One Time Verification Code:",
        widget=forms.TextInput(
            attrs={
                "placeholder": "enter the code",
                "class": "h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]",
            }
        ),
        help_text="if you didn’t receive the code, check your spam folder. Or use the resend button",
    )
