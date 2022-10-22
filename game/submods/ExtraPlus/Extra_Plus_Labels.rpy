#===========================================================================================
# RETURN_LABELS
#===========================================================================================

label view_extraplus:
    python:
        player_zoom = store.mas_sprites.zoom_level
        store.disable_zoom_button = False
        mas_RaiseShield_dlg()
        extra_button_zoom()
        Extraplus_show()
    return

label screen_extraplus:
    show monika idle at t11
    python:
        store.disable_zoom_button = False
        Extraplus_show()
    return
    
label close_extraplus:
    show monika idle at t11
    python:
        store.mas_sprites.zoom_level = player_zoom
        mas_DropShield_dlg()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label show_boop_screen:
    show monika staticpose at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
    call screen boop_revamped
    return

label return_boop_screen:
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = player_zoom
        store.mas_sprites.adjust_zoom()
    jump screen_extraplus
    return

label close_boop_screen:
    show monika idle at t11
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = player_zoom
        store.mas_sprites.adjust_zoom()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label hide_images_psr:
    hide e_rock
    hide e_paper
    hide e_scissors
    hide e_rock_1
    hide e_paper_1
    hide e_scissors_1
    $ your_choice = 0
    call screen PSR_mg
    return

label extra_restore_bg(label="ch30_visual_skip"):
    python:
        mas_extra_location(locate=False)
        disable_button_zoom()
        HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call spaceroom(scene_change=True)
    python:
        HKBShowButtons()
        renpy.jump(label)
    return

#===========================================================================================
# Label
#===========================================================================================

#====Cafe

label go_to_cafe:
    python:
        validate_files(cafe_sprite, type=False)
        mas_extra_location(locate=True)
        extra_seen_label("cafe_sorry_player", "gtcafev2", "check_label_cafe")

label check_label_cafe:
    pass

label gtcafe:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Do you want to go to the cafe?"
        m 3hub "Glad to hear it [player]!"
        m 1hubsa "I know this appointment will be great!"
        m 1hubsb "Okay, let's go [mas_get_player_nickname()]~"
        jump cafe_init

    elif mas_isNightNow():
        m 3sub "Oh, you want to go out to the cafe?"
        m 3hub "It's pretty sweet that you decided to go tonight."
        m 1eubsa "This date night is going to be great!"
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Another time then, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label gtcafev2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Do you want to go to the cafe again?"
        m 2hub "The previous time we went, I had a lot of fun!"
        m 2eubsa "So glad to hear it [player]!"
        m 1hubsb "Well, let's go [mas_get_player_nickname()]~"
        jump cafe_init
    elif mas_isNightNow():
        m 3wub "Oh, do you want to go out to the cafe again?"
        m 2hub "The previous time we went, it was very romantic~"
        m 2eubsa "So glad to go again [player]!"
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Next time then, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label cafe_talkdemo:
    show monika staticpose at t21
    python:
        store.disable_zoom_button = True
        cafe_menu = [
            ("How are you today?", 'extra_talk_feel'),
            ("What's your greatest ambition?", 'extra_talk_ambition'),
            ("Our communication is very limited, don't you think?", 'extra_talk_you'),
            ("How do you see us in 10 years?", 'extra_talk_teen'),
            ("What is your best memory that you currently have?", 'extra_talk_memory'),
            ("Do you have any phobia?", 'extra_talk_phobia'),
            ("Can we leave?", 'cafe_leave')
        ] 
    call screen list_scrolling(cafe_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"to_cafe_loop",close=False) nopredict
    return

label to_cafe_loop:
    show monika staticpose at t11
    $ store.disable_zoom_button = False
    call screen dating_loop(extraplus_acs_emptyplate, extraplus_acs_emptycup, "cafe_talkdemo", "monika_no_dessert", "monika_boopcafebeta", boop_enable=True)
    return

label cafe_leave:
    show monika 1hua at t11
    m 1eta "Oh, you want us to go back?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
    jump cafe_hide_acs

label comment_cafe:
    m 1hubsa "Thank you for asking me out."
    m 1eubsb "It is nice to have these moments as a couple!"
    m 1eubsa "I feel very fortunate to have met you and that you keep choosing me every day."
    m 1ekbsa "I love you, [mas_get_player_nickname()]!"
    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_visual_skip
    return

#====Restaurant====#

label go_to_restaurant:
    python:
        validate_files(restaurant_sprite, type=False)
        mas_extra_location(locate=True)
        extra_seen_label("restaurant_sorry_player", "gtrestaurantv2", "check_label_restaurant")

label check_label_restaurant:
    pass

label gtrestaurant:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Oh,{w=0.3} you want to go out to a restaurant?"
        m 3hub "I'm so happy to hear that,{w=0.3} [player]!"
        m "It's so sweet of you to treat me to a date."
        if mas_anni.isAnni():
            m "And on our anniversary no less,{w=0.3} perfect timing [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsa "I just know it'll be great!"
        m 1hubsb "Okay,{w=0.3} let's go [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3sub "Oh,{w=0.3} you want to go out to a restaurant?"
        m "That's so sweet of you to treat me to a date."
        if mas_anni.isAnni():
            m "And on our anniversary no less,{w=0.3} perfect timing [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsb "Let's go [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Another time then,{w=0.3} [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label gtrestaurantv2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Oh, you want to go out to the restaurant again?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~ I'm still thinking about the time you took us there for our anniversary,"
            extend " I thought it was so romantic~"
            m "So I'm glad we get to go again~!"
        else: 
            m 2hub "The last time we went, I had so much fun!"
            m 2eubsa "So I'm glad to hear it [player]!"
        m 1hubsb "Well, let's go then [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3wub "Oh, you want to go out out to the restaurant again?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~{w=0.3} I'm still thinking about the time you took us there for our anniversary,"
            extend "You really know how to make our night amazing!"
            m "So I'm glad we get to go again~!"
        else: 
            m 2hub "The last time we went, it was so romantic~"
            m 2eubsa "So I'm glad to go again [player]!"
        m 1hubsb "Let's go then [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Next time then, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label restaurant_talk:
    show monika staticpose at t21
    python:
        store.disable_zoom_button = True
        restaurant_menu = [
            ("How are you doing, [m_name]?", 'extra_talk_doing'),
            ("If you could live anywhere, where would it be?", 'extra_talk_live'),
            ("What would you change about yourself if you could?", 'extra_talk_change'),
            ("If you were a super-hero, what powers would you have?", 'extra_talk_superhero'),
            ("Do you have a life motto?", 'extra_talk_motto'),
            ("Aside from necessities, what's the one thing you couldn't go a day without?", 'extra_talk_without'),
            ("Is your glass half full or half empty?", 'extra_talk_glass'),
            ("What annoys you most?", 'extra_talk_annoy'),
            ("Describe yourself in three words.", 'extra_talk_3words'),
            ("What do you think is the first thing to pop into everyone's minds when they think about you?", 'extra_talk_pop'),
            ("If you were an animal, what animal would you be?", 'extra_talk_animal'),
            ("Can we leave?", 'restaurant_leave')
        ] 
    call screen list_scrolling(restaurant_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"to_restaurant_loop",close=False) nopredict
    return

label to_restaurant_loop:
    show monika staticpose at t11
    $ store.disable_zoom_button = False
    call screen dating_loop(extraplus_acs_pudding, extraplus_acs_icecream, "restaurant_talk","monika_no_food", "monika_booprestaurantbeta", boop_enable=True)
    return

label restaurant_leave:
    show monika 1hua at t11
    m 1eta "Oh,{w=0.3} you're ready for us to leave?"
    m 1eub "Sounds good to me!"
    m 3hua "But before we go..."
    jump restaurant_hide_acs

#===========================================================================================
# Others
#===========================================================================================
#====Cafe====#

label monika_no_dessert:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        python:
            monika_chr.remove_acs(extraplus_acs_fruitcake)
            monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Wow, I finished my fruitcake."
        m 1eub "I really enjoyed it~"
    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        python:
            monika_chr.remove_acs(extraplus_acs_chocolatecake)
            monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Wow, I finished my chocolate cake."
        m 1sua "It tasted so sweet~"
    if monika_chr.is_wearing_acs(extraplus_acs_coffeecup):
        python:
            monika_chr.remove_acs(extraplus_acs_coffeecup)
            monika_chr.wear_acs(extraplus_acs_emptycup)
        m 3dub "Also, this coffee was also good."
    if dessert_player == True:
        m 1etb "By the way, have you finished your dessert yet?{nw}"
        $ _history_list.pop()
        menu:
            m "By the way, have you finished your dessert yet?{fast}"
            "Yes":
                m 1hubsa "Ehehe~"
                m 1hubsb "I hope you enjoyed it!"
            "Not yet":
                m 1eubsa "Don't worry, eat slowly."
                m 1eubsb "I wait for you patiently~"
    else:
        m 1ekc "You told me not to worry."
        m 1ekb "But, I guess you at least have a cup of coffee."
    m 1hua "Let me know if you want to come back again."
    jump to_cafe_loop
    return

label cafe_hide_acs:
    #Code inspired by YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eub "I have to put this fruitcake away."
            m 3eub "Also, I'll put this cup away, I won't be long."
            python:
                monika_chr.remove_acs(extraplus_acs_fruitcake)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eub "I have to put this fruitcake away, I'll be right back."
            $ monika_chr.remove_acs(extraplus_acs_fruitcake)

    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eua "I must put this chocolate cake away."
            m 3eua "Also, I'll put this cup away, it won't be long now."
            python:
                monika_chr.remove_acs(extraplus_acs_chocolatecake)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eua "I must put this chocolate cake away, I'll be right back."
            $ monika_chr.remove_acs(extraplus_acs_chocolatecake)

    elif monika_chr.is_wearing_acs(extraplus_acs_emptyplate):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3hua "I'll go put this plate away."
            m 3hua "Also, I'll put this cup away, I won't be long."
            python:
                monika_chr.remove_acs(extraplus_acs_emptyplate)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3hua "I'm going to put this plate away, give me a moment."
            $ monika_chr.remove_acs(extraplus_acs_emptyplate)

    call mas_transition_to_emptydesk
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Okay, let's go, [player]!"
    call extra_restore_bg("comment_cafe")
    return

#====Restaurant====#

label monika_no_food:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta):
        python:
            monika_chr.remove_acs(extraplus_acs_pasta)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my pasta."
        m 1eub "I really enjoyed it~"
        m "Now I'll grab some dessert. Be right back!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_icecream)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_pancakes):
        python:
            monika_chr.remove_acs(extraplus_acs_pancakes)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my pancakes."
        m 1sua "They were delicious~"
        m "Now I'll grab some dessert. Be right back!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_waffles):
        python:
            monika_chr.remove_acs(extraplus_acs_waffles)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Wow, I finished my waffles."
        m 1sua "They were delicious~"
        m "Now I'll grab some dessert. Be right back!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
        call mas_transition_from_emptydesk("monika 1eua")

    if food_player == True:
        m 1etb "By the way, have you finished your food yet?{nw}"
        $ _history_list.pop()
        menu:
            m "By the way, have you finished your food yet?{fast}"
            "Yes":
                m 1hubsa "Ehehe~"
                m 1hubsb "I hope you enjoyed it!"
            "Not yet":
                m 1eubsa "Don't worry, eat slowly."
                m 1eubsb "I wait for you patiently~"
    else:
        m 1ekc "You told me not to worry."
        m 1ekb "But, I guess you at least have a drink with you."
    m 1hua "Let me know if you want to come back again."
    jump to_restaurant_loop
    return
    
label restaurant_hide_acs:
    #Code inspired by YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_candles):
        if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_icecream):
            m 3eub "I have to put these candles away."
            m "We can never be too careful with fire!"
            m 3eub "Also, I'll put this plate away, I won't be long."
            python:
                monika_chr.remove_acs(extraplus_acs_candles)
                monika_chr.remove_acs(extraplus_acs_pasta)
                monika_chr.remove_acs(extraplus_acs_icecream)
        else:
            m 3eub "I have to put these candles away."
            m "We can never be too careful with fire!"
            $ monika_chr.remove_acs(extraplus_acs_candles)

    elif monika_chr.is_wearing_acs(extraplus_acs_flowers):
        if monika_chr.is_wearing_acs(extraplus_acs_pancakes) or monika_chr.is_wearing_acs(extraplus_acs_pudding):
            m 3eua "I must put this plate away."
            m 3eua "Also, I'll put these flowers away, I won't be long."
            python:
                monika_chr.remove_acs(extraplus_acs_flowers)
                monika_chr.remove_acs(extraplus_acs_pancakes)
                monika_chr.remove_acs(extraplus_acs_pudding)

        elif monika_chr.is_wearing_acs(extraplus_acs_waffles):
            m 3eua "I must put this plate away."
            m 3eua "Also, I'll put these flowers away, I won't be long."
            python:
                monika_chr.remove_acs(extraplus_acs_flowers)
                monika_chr.remove_acs(extraplus_acs_waffles)
        else:
            m 3eua "I'll put these flowers away, I won't be long."
            $ monika_chr.remove_acs(extraplus_acs_flowers)

    call mas_transition_to_emptydesk
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Okay, let's go, [player]!"
    call extra_restore_bg
    return

################################################################################
## MENUS
################################################################################

label walk_extra:
    show monika idle at t21
    python:
        store.disable_zoom_button = True
        monika_talk = renpy.substitute(renpy.random.choice(date_talk))
        renpy.say(m, monika_talk, interact=False)
    call screen list_scrolling(walk_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"screen_extraplus",close=True) nopredict
    return

label minigames_extra:
    show monika idle at t21
    python:
        store.disable_zoom_button = True
        m_talk = renpy.substitute(renpy.random.choice(minigames_talk))
        renpy.say(m, m_talk, interact=False)
    call screen list_generator(minigames_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"screen_extraplus",close=True) nopredict
    return

label tools_extra:
    show monika idle at t21
    $ store.disable_zoom_button = True
    call screen list_scrolling(tools_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"screen_extraplus",close=True) nopredict
    return

################################################################################
## GIFTS
################################################################################

label make_gift:
    show monika idle at t21
    python:
        gift_menu = [
            ("Customized gift", 'make_file'),
            ("Groceries", 'groceries'),
            ("Objects", 'objects'),
            ("Ribbons", 'ribbons')
        ]
    call screen list_scrolling(gift_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN,"tools_extra",close=True) nopredict
    return

label make_file:
    show monika idle at t11
    python:
        import os
        makegift = mas_input(_("Enter the name of the gift."),
                            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
                            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"})
        if not makegift:
            renpy.jump("make_file")
        else:
            if makegift == "cancel":
                renpy.jump("make_gift")
            else:
                filepath = os.path.join(renpy.config.basedir + '/characters', makegift + '.gift')
                f = open(filepath,"a")
                renpy.notify("Has been successfully created.")
                renpy.jump("make_gift")
    return

label groceries:
    show monika idle at t21
    python:
        groceries_menu = [
            extra_gift("Coffee", 'coffee.gift', gift_append),
            extra_gift("Chocolates", 'chocolates.gift', gift_append),
            extra_gift("Cupcake", 'cupcake.gift', gift_append),
            extra_gift("Fudge", 'fudge.gift', gift_append),
            extra_gift("Hot Chocolate", 'hotchocolate.gift', gift_append),
            extra_gift("Candy", 'candy.gift', gift_append),
            extra_gift("Candy Canes", 'candycane.gift', gift_append),
            extra_gift("Candy Corn", 'candycorn.gift', gift_append),
            extra_gift("Christmas Cookies", 'christmascookies.gift', gift_append)
        ]
        
    call screen list_generator(groceries_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, "make_gift", close=True) nopredict
    return

label objects:
    show monika idle at t21
    python:
        objects_menu = [
            extra_gift("Promise Ring", 'promisering.gift', gift_append),
            extra_gift("Roses", 'roses.gift', gift_append),
            extra_gift("Quetzal Plushie", 'quetzalplushie.gift', gift_append),
            extra_gift("Thermos Mug", 'justmonikathermos.gift', gift_append)
        ]

    call screen list_generator(objects_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, "make_gift", close=True) nopredict
    return
            
label ribbons:
    show monika idle at t21
    python:
        ribbons_menu = [
            extra_gift("Black Ribbon", 'blackribbon.gift', gift_append),
            extra_gift("Blue Ribbon", 'blueribbon.gift', gift_append),
            extra_gift("Dark Purple Ribbon", 'darkpurpleribbon.gift', gift_append),
            extra_gift("Emerald Ribbon", 'emeraldribbon.gift', gift_append),
            extra_gift("Gray Ribbon", 'grayribbon.gift', gift_append),
            extra_gift("Green Ribbon", 'greenribbon.gift', gift_append),
            extra_gift("Light Purple Ribbon", 'lightpurpleribbon.gift', gift_append),
            extra_gift("Peach Ribbon", 'peachribbon.gift', gift_append),
            extra_gift("Pink Ribbon", 'pinkribbon.gift', gift_append),
            extra_gift("Platinum Ribbon", 'platinumribbon.gift', gift_append),
            extra_gift("Red Ribbon", 'redribbon.gift', gift_append),
            extra_gift("Ruby Ribbon", 'rubyribbon.gift', gift_append),
            extra_gift("Sapphire Ribbon", 'sapphireribbon.gift', gift_append),
            extra_gift("Silver Ribbon", 'silverribbon.gift', gift_append),
            extra_gift("Teal Ribbon", 'tealribbon.gift', gift_append),
            extra_gift("Yellow Ribbon", 'yellowribbon.gift', gift_append)
        ]
        
    call screen list_generator(ribbons_menu, mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, "make_gift", close=True) nopredict
    return
