<script>
</script>

<!--

    _="
           on hyperscript:change_background
           add .backdrop-blur to <backdrop/> in me
           then wait 300ms
           js(previous_item)
            
           const random_anime = (arr => {
           const len = arr == null ? 0 : arr.length
           return len ? arr[Math.floor(Math.random() * len)] : undefined
           })(Array.from([{'name': 'Demon Slayer', 'cover': '/static/public/images/mock/DemonSlayer-cover.avif'}, {'name': 'Hyouka', 'cover': '/static/public/images/mock/Hyouka-bg.avif'}, {'name': 'You Lie in April', 'cover': '/static/public/images/mock/YourLieInApril-bg.avif'}, {'name': 'Attack on Titan', 'cover': '/static/public/images/mock/AttackOnTitan-bg.avif'}, {'name': 'Jujutsu Kaisen', 'cover': '/static/public/images/mock/JujutsuKaisen.avif'}, {'name': 'Death Note', 'cover': '/static/public/images/mock/DeathNote-bg.avif'}]).filter(item => item !== previous_item))
           return random_anime
           end
           set local previous_item to it
           send change(image:previous_item.cover) to <img/> in me
           send change(anime_name:previous_item.name) to <anime-name/> in me
           then remove .backdrop-blur from <backdrop/> in me

           init
           repeat forever
           trigger hyperscript:change_background
           then wait 10s
           end
          "
-->

<div class="relative grid h-screen w-screen bg-secondary md:grid-cols-2">
    <SideImage />
    <div class="absolute inset-x-0 self-end rounded-t-3xl bg-secondary p-7 md:static md:self-auto md:rounded-t-none md:p-0 md:px-[8vw] md:py-[2.2vw]">
        <form
            class="flex h-max w-full flex-col gap-10 md:h-full md:justify-between md:rounded-none md:p-0"
            hx-post="/user/register/"
            hx-target="this"
            enctype="application/x-www-form-urlencoded"
        >
            <content class="contents">
                <script
                    type="module"
                    src="http://localhost:5173/static/js/register.ts"
                ></script>

                <div class="flex flex-col gap-2 whitespace-nowrap font-bold uppercase leading-none tracking-widest text-white md:gap-[0.5vw] md:text-[1.2vw]">
                    <span class="inline-flex gap-2 md:gap-[0.5vw]">
                        create your
                        <coreproject-icon-core-text>
                            <p
                                class="inline-flex"
                                style=""
                            >
                                <span class="text-white/90">c</span>
                                <span class="text-warning">o</span>
                                <span class="text-white/90">r</span>
                                <span class="text-white/90">e</span>
                            </p>
                        </coreproject-icon-core-text>
                        account
                    </span>
                    <span class="text-xs font-medium uppercase text-white/90 md:text-[1vw]">unlock the anime world - join us!</span>
                </div>
                <!--
    _="
   init
   set global validator to {'length': false, 'special': false, 'number': false, 'lower_or_upper': false}
  "
-->
                <div class="flex flex-col gap-5 md:gap-[1.5vw]">
                    <email-field class="flex flex-col gap-1 md:gap-[0.5vw]">
                        <label
                            for="email"
                            class="mt-4 text-lg font-semibold leading-none md:mt-[1.1vw] md:text-[1.1vw]"
                        >
                            Email:
                        </label>
                        <input
                            type="text"
                            name="email"
                            placeholder="sora_amamiya@coreproject.moe"
                            class="h-12 w-full rounded-xl border-2 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"
                            maxlength="320"
                            aria-describedby="id_email_helptext"
                            id="id_email"
                        />
                        <span class="mt-[0.75vw] text-xs leading-none text-base-content md:mt-0 md:text-[0.75vw]">we’ll send you a verification email, so please ensure it’s active</span>
                    </email-field>
                    <div class="flex flex-col gap-1 md:gap-[0.5vw]">
                        <label
                            for="password"
                            class="text-lg font-semibold leading-none md:text-[1.1vw]"
                        >
                            Password:
                        </label>
                        <!--

        _="
                on keyup
                    set global password to my.value
                    js(password)
                        try{
                            return window.get_password_strength(password).score;
                        } catch (e) {
                            console.log(&quot;Silenced errors&quot;)
                            return null
                        }
                    end
                    send hyperscript:password_strength(strength:it) to <password-strength/>
            " 
    -->
                        <input
                            type="password"
                            name="password"
                            placeholder="enter your existing password"
                            class="h-12 w-full rounded-xl border-2 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"
                            id="id_password"
                        />
                        <div class="flex flex-col">
                            <!--

             _="

               on hyperscript:password_strength(strength)
               js(my, strength)
               const children_array = Array.from(my.children);

               children_array.forEach((children, index)=>{
               const bg_class = children.getAttribute('bg_class');
               children.classList.remove(bg_class);
               })

               children_array.splice(0,strength).forEach((children,index)=>{
               const bg_class = children.getAttribute('bg_class');
               children.classList.add(bg_class);
               });
               end
              "
        -->
                            <password-strength class="grid grid-cols-4 gap-[1.5vw] md:gap-[0.75vw]">
                                <span
                                    bg_class="bg-blue-800"
                                    class="h-[1.75vw] rounded-[0.5vw] border-white/25 transition-colors md:h-[0.75vw] md:rounded-[0.1875vw] md:border-[0.15vw]"
                                ></span>
                                <span
                                    bg_class="bg-blue-700"
                                    class="h-[1.75vw] rounded-[0.5vw] border-white/25 transition-colors md:h-[0.75vw] md:rounded-[0.1875vw] md:border-[0.15vw]"
                                ></span>
                                <span
                                    bg_class="bg-blue-600"
                                    class="h-[1.75vw] rounded-[0.5vw] border-white/25 transition-colors md:h-[0.75vw] md:rounded-[0.1875vw] md:border-[0.15vw]"
                                ></span>
                                <span
                                    bg_class="bg-blue-500"
                                    class="h-[1.75vw] rounded-[0.5vw] border-white/25 transition-colors md:h-[0.75vw] md:rounded-[0.1875vw] md:border-[0.15vw]"
                                ></span>
                            </password-strength>
                            <div class="mt-3 md:mt-[1.25vw]">
                                <span class="text-surface-50 text-sm font-semibold uppercase leading-none tracking-wider md:text-[1vw]">must contain</span>
                                <div class="ml-2 mt-[0.4vw] flex flex-col gap-[0.1vw] md:w-3/5">
                                    <div>
                                        <div class="flex flex-col gap-1 md:gap-[0.3vw]">
                                            <!--
                            _="
                               on keyup from #id_password
                               if it.value.length >= 8
                               set global validator.length to true
                               remove .opacity-30 from <svg/> in me
                               else
                               set global validator.length to false
                               add .opacity-30 to <svg/> in me
                              "
                        -->
                                            <div class="flex items-center gap-2 md:gap-[0.5vw]">
                                                <coreproject-icon-tick class="w-3 text-primary opacity-30 transition-opacity md:w-[0.7vw]">
                                                    <svelte-retag>
                                                        <svg
                                                            class="w-3 text-primary opacity-30 transition-opacity md:w-[0.7vw]"
                                                            style=""
                                                            viewBox="0 0 24 24"
                                                            fill="none"
                                                            xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                            <path
                                                                d="M4.89163 13.2687L9.16582 17.5427L18.7085 8"
                                                                stroke="currentColor"
                                                                stroke-width="2.5"
                                                                stroke-linecap="round"
                                                                stroke-linejoin="round"
                                                            ></path>
                                                        </svg>
                                                        <!--<Index>-->
                                                    </svelte-retag>
                                                </coreproject-icon-tick>
                                                <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.75vw]">minimum 8 characters</span>
                                            </div>
                                            <!--
                            _="
                               on keyup from #id_password
                               js(it)
                               return new RegExp(/[!@#$%^&amp;*()_+{}\[\]:;<>,.?\\]/).test(it.value)
                               end
                               if it
                               set global validator.special to true
                               remove .opacity-30 from <svg/> in me
                               else
                               set global validator.special to false
                               add .opacity-30 to <svg/> in me
                               end
                              "
                        -->
                                            <div class="flex items-center gap-2 md:gap-[0.5vw]">
                                                <coreproject-icon-tick class="w-3 text-primary opacity-30 transition-opacity md:w-[0.7vw]">
                                                    <svelte-retag>
                                                        <svg
                                                            class="w-3 text-primary opacity-30 transition-opacity md:w-[0.7vw]"
                                                            style=""
                                                            viewBox="0 0 24 24"
                                                            fill="none"
                                                            xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                            <path
                                                                d="M4.89163 13.2687L9.16582 17.5427L18.7085 8"
                                                                stroke="currentColor"
                                                                stroke-width="2.5"
                                                                stroke-linecap="round"
                                                                stroke-linejoin="round"
                                                            ></path>
                                                        </svg>
                                                        <!--<Index>-->
                                                    </svelte-retag>
                                                </coreproject-icon-tick>
                                                <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.75vw]">minimum 1 special character</span>
                                            </div>
                                            <!--

                            _="
                               on keyup from #id_password
                               js(it)
                               return new RegExp(/\d/).test(it.value)
                               end
                               if it
                               set global validator.number to true
                               remove .opacity-30 from <svg/> in me
                               else
                               set global validator.number to false
                               add .opacity-30 to <svg/> in me
                               end
                              "
                        -->
                                            <div class="flex items-center gap-2 md:gap-[0.5vw]">
                                                <coreproject-icon-tick class="w-3 text-primary opacity-30 transition-opacity md:w-[0.7vw]">
                                                    <svelte-retag>
                                                        <svg
                                                            class="w-3 text-primary opacity-30 transition-opacity md:w-[0.7vw]"
                                                            style=""
                                                            viewBox="0 0 24 24"
                                                            fill="none"
                                                            xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                            <path
                                                                d="M4.89163 13.2687L9.16582 17.5427L18.7085 8"
                                                                stroke="currentColor"
                                                                stroke-width="2.5"
                                                                stroke-linecap="round"
                                                                stroke-linejoin="round"
                                                            ></path>
                                                        </svg>
                                                        <!--<Index>-->
                                                    </svelte-retag>
                                                </coreproject-icon-tick>
                                                <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.75vw]">minimum 1 number</span>
                                            </div>
                                            <!--
                                                 _="
                               on keyup from #id_password
                               js(it)
                               return new RegExp(/[a-zA-Z]/).test(it.value)
                               end
                               if it
                               set global validator.lower_or_upper to true
                               remove .opacity-30 from <svg/> in me
                               else
                               set global validator.lower_or_upper to false
                               add .opacity-30 to <svg/> in me
                               end
                              "
                                            -->
                                            <div class="flex items-center gap-2 md:gap-[0.5vw]">
                                                <coreproject-icon-tick class="w-3 text-primary opacity-30 transition-opacity md:w-[0.7vw]">
                                                    <svelte-retag>
                                                        <svg
                                                            class="w-3 text-primary opacity-30 transition-opacity md:w-[0.7vw]"
                                                            style=""
                                                            viewBox="0 0 24 24"
                                                            fill="none"
                                                            xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                            <path
                                                                d="M4.89163 13.2687L9.16582 17.5427L18.7085 8"
                                                                stroke="currentColor"
                                                                stroke-width="2.5"
                                                                stroke-linecap="round"
                                                                stroke-linejoin="round"
                                                            ></path>
                                                        </svg>
                                                        <!--<Index>-->
                                                    </svelte-retag>
                                                </coreproject-icon-tick>
                                                <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.75vw]">minimum 1 lower-case or upper-case character</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-col gap-[0.3rem] md:gap-[0.5vw]">
                        <label
                            for="confirm-password"
                            class="text-lg font-semibold leading-none md:text-[1.1vw]"
                        >
                            Confirm Password:
                        </label>
                        <input
                            type="password"
                            name="confirm_password"
                            placeholder="re-enter your password"
                            class="h-12 w-full rounded-xl border-2 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"
                            aria-describedby="id_confirm_password_helptext"
                            id="id_confirm_password"
                        />
                        <span class="text-xs leading-none md:text-[0.75vw]">Please make sure you enter the same password in both fields</span>
                    </div>
                </div>
                <div class="flex items-center justify-between">
                    <div class="flex flex-col gap-1 md:gap-[0.5vw]">
                        <span class="text-surface-100 text-xs leading-none md:text-[0.75vw]">Already have an account?</span>
                        <!-- <button
                            hx-get="/user/login/"
                            hx-push-url="/user/login/"
                            hx-target="<content/>"
                            class="text-start text-base leading-none text-primary underline md:text-[1.1vw]"
                        >
                            Login
                        </button> -->
                    </div>
                    <button
                        type="submit"
                        class="btn btn-primary h-max min-h-max rounded-lg p-4 text-base font-semibold leading-none text-accent md:rounded-[0.5vw] md:p-[1vw] md:text-[0.95vw]"
                    >
                        <span>Continue</span>
                        <coreproject-icon-arrow-up-right class="w-4 rotate-45 md:w-[1vw]">
                            <svelte-retag>
                                <svg
                                    class="w-4 rotate-45 md:w-[1vw]"
                                    style=""
                                    viewBox="0 0 16 16"
                                    fill="none"
                                    xmlns="http://www.w3.org/2000/svg"
                                >
                                    <path
                                        d="M4.66699 11.3333L11.3337 4.66666"
                                        stroke="currentColor"
                                        stroke-width="2"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                    ></path>
                                    <path
                                        d="M4.66699 4.66666H11.3337V11.3333"
                                        stroke="currentColor"
                                        stroke-width="2"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                    ></path>
                                </svg>
                                <!--<Index>-->
                            </svelte-retag>
                        </coreproject-icon-arrow-up-right>
                    </button>
                </div>
            </content>
        </form>
    </div>
</div>
