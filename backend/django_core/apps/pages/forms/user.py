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


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label="Email:",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "sora_amamiya@coreproject.moe",
                "class": "h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
            }
        ),
        help_text="Please enter a valid email address",
    )
    password1 = forms.CharField(
        label="Password:",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "enter your existing password",
                "class": "h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password:",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "re-enter your password",
                "class": "h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
            }
        ),
    )
