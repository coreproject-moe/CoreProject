<form class="bg-surface-900 flex h-max w-full flex-col gap-[15vw] p-10 md:h-full md:justify-between md:gap-0 md:rounded-none md:p-0">
    <content class="contents">
        <div class="flex flex-col gap-2 whitespace-nowrap font-bold uppercase leading-none tracking-widest text-white md:gap-[0.5vw] md:text-[1.2vw]">
            <span class="text-base font-bold uppercase tracking-widest md:text-[1.2vw]">forgot password? don't worry!</span>
            <span class="font-medium uppercase text-white/90 md:text-[1vw]">Reclaim Your Anime Journey</span>
        </div>
        <div class="flex flex-col gap-[0.3rem] md:gap-[0.5vw]">
            <label class="text-base font-semibold leading-none md:text-[1.1vw]">Email</label>
            <!-- {{ form.email }} -->
            <div class="flex items-center gap-2 md:gap-[0.5vw]">
                <coreproject-icon-info class="w-3 opacity-70 md:w-[0.9vw]"></coreproject-icon-info>

                <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.8vw]">
                    <!-- {% if form.email.errors %}
                    <coreproject-markdown markdown="{{form.email.errors|first}}"></coreproject-markdown>
                {% else %}
                    {{ form.email.help_text }}
                {% endif %} -->
                </span>
            </div>
        </div>
        <div class="flex items-center justify-between">
            <div class="flex flex-col gap-1 md:gap-[0.5vw]">
                <span class="text-surface-100 text-xs leading-none md:text-[0.75vw]">Don't have a core account?</span>
                <!-- <button
                hx-get="{% url 'register_view' %}"
                hx-push-url="{% url 'register_view' %}"
                hx-target="<content/>"
                class="text-start text-base leading-none md:text-[1.1vw] text-primary underline"
            >
                Register
            </button> -->
            </div>
            <button
                type="submit"
                class="btn btn-primary h-12 rounded-lg p-0 px-5 text-base font-semibold leading-none text-accent md:h-[2.75vw] md:rounded-[0.5vw] md:px-[1.25vw] md:text-[0.95vw]"
            >
                <span>Continue</span>
                <coreproject-icon-arrow-up-right class="w-4 rotate-45 md:w-[1vw]"></coreproject-icon-arrow-up-right>
            </button>
        </div>
    </content>
</form>
