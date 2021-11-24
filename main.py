import tkinter as tk
import random
from tkinter import ttk
import dataset as ds  # to carry out data retrieval process

stall_type = ds.stall_type()  # return type of the stall

# message to be shown in the chatbot
to_show = "Hello! Welcome to Food Ordering Chatbot! Please type out the stall name first: \n 1. {0}\n 2. {1}\n " \
          "3. {2}\n 4. {3}\n 5. {4}\n\n".format(*stall_type)

item_price = []  # empty item_price list to store price of the item after user select
item_cart = []  # empty item_cart list to store the food after user select


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        bg_colour = '#feffe0'
        font_type = 'Calibri'
        global to_show
        global item_price, item_cart
        btn_colour = '#e3a28d'

        def dropdown(food_dict, list_menu):
            """Display menu selection

            Parameters:
            food_dict: dictionary
                food as key while price and delivery services are values
            list_menu: list
                to be displayed in dropdown menu
            """

            def print_to_convowindow():
                # input to convo_log
                convo_log.config(state=tk.NORMAL)
                food = selected_item.get()
                convo_log.insert(tk.END, "You: " + food + '\n\n')
                convo_log.config(state=tk.DISABLED)
                convo_log.see(tk.END)  # .see(tk.END) is used to show user the latest msg printed on convo_log
                dropdown_menu.destroy()
                submit_button.destroy()
                back_button.destroy()
                chatbot_application(food)

            def back():
                """ let the user to go back to stall selection
                """
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Back")
                convo_log.config(state=tk.DISABLED)
                convo_log.see(tk.END)
                dropdown_menu.destroy()
                submit_button.destroy()
                back_button.destroy()
                stall_selection()

            def chatbot_application(food):
                """Perform Chatbot Application

                Parameters:
                food: string
                    food that obtained from print_to_convowindow()
                    to continue process of chatbot application such as appending the item_cart list

                """

                def check_cart(stl_btn, chk_btn):
                    """To check item_cart

                    Parameters:
                    stl_btn: Tkinter button widget
                       to be destroyed in this function
                    chk_btn: Tkinter button widget
                        to be destroyed in this function
                    """

                    if not item_cart:
                        exit_program(stl_btn, chk_btn)

                    else:
                        stl_btn.destroy()
                        chk_btn.destroy()
                        convo_log.config(state=tk.NORMAL)
                        convo_log.insert(tk.END, "\n\nYou: Exit\n\nBot: Are you sure you want to exit?\n"
                                                 "You still have item in cart for self pickup, do you    wish to checkout?\n"
                                                 "Press [Exit] if you wish to exit\n"
                                                 "Press [Check Out] if you wish to check out")
                        convo_log.config(state=tk.DISABLED)
                        convo_log.see(tk.END)
                        exit_button = tk.Button(self, text='Exit', font=(font_type, 14), bg=bg_colour)
                        exit_button.place(x=100, y=401)

                        checkout_button = tk.Button(self, text='Check Out', font=(font_type, 14), bg=bg_colour)
                        checkout_button.place(x=180, y=401)
                        exit_button['command'] = lambda exit_btn=exit_button, checkout_btn=checkout_button: exit_program(exit_btn, checkout_btn)
                        checkout_button['command'] = lambda exit_btn=exit_button, checkout_btn=checkout_button: checkout(exit_btn, checkout_btn)

                def exit_program(stl_btn, chk_btn):
                    stl_btn.destroy()
                    chk_btn.destroy()
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Exit\n\nBot: Goodbye and see you again.")
                    convo_log.config(state=tk.DISABLED)
                    convo_log.see(tk.END)

                    # program exit after 3 seconds
                    self.after(3000, lambda: self.destroy())

                def click_delete(stl_btn, chk_btn):
                    """To destroy buttons and proceed to stall_selection()

                     Parameters:
                     stl_btn: Tkinter button widget
                        to be destroyed in this function
                     chk_btn: Tkinter button widget
                         to be destroyed in this function
                     """

                    stall_selection()
                    stl_btn.destroy()
                    chk_btn.destroy()

                def self_pickup_click_delete(yes_btn, menu_btn, stall_select_btn):
                    """Proceed to self_pickup()

                     Parameters:
                     yes_btn: Tkinter button widget
                        to be destroyed in this function
                     menu_btn: Tkinter button widget
                        to be destroyed in this function
                     stall_select_btn: Tkinter button widget
                        to be destroyed in this function
                     """

                    item_price.append(food_price)
                    item_cart.append(food)
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Self Pick Up")
                    convo_log.config(state=tk.DISABLED)
                    convo_log.see(tk.END)
                    self_pickup()
                    yes_btn.destroy()  # buttons are destroyed using destroy() from tkinter
                    menu_btn.destroy()
                    stall_select_btn.destroy()

                def menu_click_delete(yes_btn, menu_btn, stall_select_btn):
                    """Proceed to dropdown(food_dict, list_menu)

                     Parameters:
                     yes_btn: Tkinter button widget
                        to be destroyed in this function
                     menu_btn: Tkinter button widget
                        to be destroyed in this function
                     stall_select_btn: Tkinter button widget
                        to be destroyed in this function
                     """
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Menu")  # input to convo_log
                    convo_log.config(state=tk.DISABLED)
                    convo_log.see(tk.END)
                    yes_btn.destroy()
                    menu_btn.destroy()
                    stall_select_btn.destroy()
                    dropdown(food_dict, list_menu)

                def stall_click_delete(yes_btn, menu_btn, stall_select_btn):
                    """Proceed to stall_selection()

                     Parameters:
                     yes_btn: Tkinter button widget
                        to be destroyed in this function
                     menu_btn: Tkinter button widget
                        to be destroyed in this function
                     stall_select_btn: Tkinter button widget
                        to be destroyed in this function
                     """
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Stall Selection")
                    convo_log.config(state=tk.DISABLED)
                    convo_log.see(tk.END)
                    yes_btn.destroy()
                    menu_btn.destroy()
                    stall_select_btn.destroy()
                    stall_selection()

                def delivery_yes_delete(self_pickup_btn, delivery_btn):
                    """Proceed to self_pickup even delivery service is provided

                     Parameters:
                     self_pickup_btn: Tkinter button widget
                        to be destroyed in this function
                     delivery_btn: Tkinter button widget
                        to be destroyed in this function
                     """
                    # append the global item_price and item_cart here with the food that user selected
                    item_price.append(food_price)
                    item_cart.append(food)

                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Self Pick Up\n\n")
                    convo_log.config(state=tk.DISABLED)
                    convo_log.see(tk.END)
                    self_pickup_btn.destroy()
                    delivery_btn.destroy()
                    self_pickup()

                def checkout_click_delete(chk_stl_btn, chk_chk_btn):
                    """Proceed to stall_selection() after checkout()

                     Parameters:
                     chk_stl_btn: Tkinter button widget
                        to be destroyed in this function
                     chk_chk_btn: Tkinter button widget
                        to be destroyed in this function
                     """
                    # clear the list after user select checkout
                    item_price.clear()
                    item_cart.clear()

                    stall_selection()
                    chk_chk_btn.destroy()
                    chk_stl_btn.destroy()

                def delivery_click_delete(del_stl_btn, del_chk_btn):
                    """Proceed to stall_selection()

                     Parameters:
                     del_stl_btn: Tkinter button widget
                        to be destroyed in this function
                     del_chk_btn: Tkinter button widget
                        to be destroyed in this function
                     """
                    del_stl_btn.destroy()
                    del_chk_btn.destroy()
                    stall_selection()

                def checkout(stl_btn, chk_btn):
                    """Perform checkout application

                     Parameters:
                     stl_btn: Tkinter button widget
                        to be destroyed in this function
                     chk_btn: Tkinter button widget
                        to be destroyed in this function
                     """
                    stl_btn.destroy()
                    chk_btn.destroy()
                    order_num = random.sample(range(5000), 1)  # order number to user to collect food at the stall
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Check Out")
                    convo_log.see(tk.END)
                    # Calculate the price in item_price list, thus letting total_price = 0
                    total_price = 0
                    for i in item_price:
                        total_price += i

                    # Joining items in item_cart, then print out to the convo_log
                    item = '\n'.join([str(i) for i in item_cart])
                    convo_log.insert(tk.END, "\n\nBot: You have successfully ordered " + item
                                     + "\ntotal price is: RM"
                                     + str(total_price)
                                     + "\nBot: Here is your order number: " + str(order_num)
                                     + "\nPlease pay and collect at counter")
                    convo_log.see(tk.END)
                    convo_log.insert(tk.END, '\n\nBot: Do you wish to order food again? '
                                             '\nPress [stall selection] to view the stall,'
                                             '\n[Exit] to quit')
                    convo_log.see(tk.END)
                    convo_log.config(state=tk.DISABLED)

                    # exit button and stall_button under checkout function, thus chkout_exit_btn and chkout_stall_button
                    chkout_exit_btn = tk.Button(self, text="Exit", font=(font_type, 14), bg=btn_colour)
                    chkout_exit_btn.place(x=250, y=401, height=50)
                    chkout_stall_button = tk.Button(self, text="Stall Selection", font=(font_type, 14),
                                                    bg=btn_colour)
                    chkout_stall_button.place(x=80, y=401, height=50)
                    chkout_stall_button['command'] = lambda chk_stl_btn=chkout_stall_button, chk_exit_btn=chkout_exit_btn: checkout_click_delete(
                        chk_stl_btn, chk_exit_btn)
                    chkout_exit_btn['command'] = lambda chk_stl_btn=chkout_stall_button, chk_exit_btn=chkout_exit_btn: exit_program(chk_stl_btn, chk_exit_btn)

                    # clear the list after checkout, ensure list is empty before user proceed to another order
                    item_price.clear()
                    item_cart.clear()

                def self_pickup():
                    """ Perform Self pickup application
                    """
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nBot: You have ordered " + food +
                                     '\nand the total price is RM' + str(food_price) +
                                     '\n\nBot: Ordered Successful added into cart\n'
                                     'Bot: Do you wish to order food again? '
                                     '\nPress [stall selection] to view the stall,'
                                     '\n[Check Out] to quit\n\n')
                    convo_log.config(state=tk.DISABLED)
                    convo_log.see(tk.END)

                    # checkout button and stall selection button under self pickup function
                    # checkout_btn = checkout button while stall_btn = stall selection button
                    checkout_btn = tk.Button(self, text="Check Out", font=(font_type, 14),
                                             bg=btn_colour)
                    stall_btn = tk.Button(self, text="Stall Selection", font=(font_type, 14),
                                          bg=btn_colour)
                    stall_btn['command'] = lambda stl_btn=stall_btn, chk_btn=checkout_btn: click_delete(stl_btn, chk_btn)
                    checkout_btn.place(x=250, y=401, height=50)
                    checkout_btn['command'] = lambda stl_btn=stall_btn, chk_btn=checkout_btn: checkout(stl_btn, chk_btn)
                    stall_btn.place(x=80, y=401, height=50)

                def delivery_services():
                    """ Perform delivery application.
                    """
                    def print_text():
                        # obtain user's name, phone num and address from entry box
                        user_name = name_entry.get()
                        user_phoneno = phoneno_entry.get()
                        user_building = selected_building.get()
                        user_floor = selected_floor.get()
                        if user_floor == '-':
                            convo_log.config(state=tk.NORMAL)
                            convo_log.insert(tk.END, "\n\nBot: Incorrect address")
                            convo_log.config(state=tk.DISABLED)
                            convo_log.see(tk.END)

                        user_address = user_building + ' ' + user_floor
                        # to check if user input correct username and phone number
                        if user_name.isdigit() or user_phoneno.isalpha() or (user_name and user_phoneno == '') or (len(user_phoneno) != 10 and len(user_phoneno) != 11):
                            convo_log.config(state=tk.NORMAL)
                            convo_log.insert(tk.END, "\n\nBot: Incorrect Phone Number or Username")
                            convo_log.config(state=tk.DISABLED)
                            convo_log.see(tk.END)
                        else:
                            convo_log.config(state=tk.NORMAL)
                            convo_log.insert(tk.END, "\n\nBot: You have successfully ordered " + food
                                             + "\ntotal price is: RM"
                                             + str(food_price)
                                             + "\nBot: Do you wish to order food again? "
                                             "\nPress [Stall Selection] to view the stall,"
                                             "\n[Exit] to quit")

                            convo_log.see(tk.END)
                            convo_log.config(state=tk.DISABLED)
                            name_entry.destroy()
                            name_label.destroy()
                            send_button.destroy()
                            building_dropdown.destroy()
                            floor_dropdown.destroy()
                            phoneno_label.destroy()
                            phoneno_entry.destroy()

                            # exit button will bring user to check_cart first to check if cart is empty before exiting
                            exit_btn = tk.Button(self, text="Exit", font=(font_type, 14), bg=btn_colour)
                            exit_btn.place(x=250, y=401, height=50)

                            # stall selection button bring user to destroy button function first then only to stall_selection()
                            delivery_stall_btn = tk.Button(self, text="Stall Selection", font=(font_type, 14),
                                                           bg=btn_colour)
                            delivery_stall_btn.place(x=80, y=401, height=50)
                            delivery_stall_btn['command'] = lambda del_stl_btn=delivery_stall_btn, del_exit_btn=exit_btn: delivery_click_delete(del_stl_btn, del_exit_btn)
                            exit_btn['command'] = lambda del_stl_btn=delivery_stall_btn, del_exit_btn=exit_btn: check_cart(del_stl_btn, del_exit_btn)

                    def bind_func(selected_building):
                        """to bind the dropdown of the floor address with building dropdown

                        Paremeter:
                        selected_building: string
                            to bind with building dropdown
                        """
                        floor_dropdown.set_menu(*floor.get(selected_building))

                    # input to convo_log
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Delivery Service\n\n"
                                             "Bot: Please enter your name and phone number    then select your address")
                    convo_log.config(state=tk.DISABLED)
                    convo_log.see(tk.END)

                    # destroy() is used to destroy buttons
                    delivery_button.destroy()
                    self_pickup_button.destroy()

                    # name label
                    name_label = tk.Label(self, text="Name: ", font=(font_type, 12, 'bold'))
                    name_label.place(x=85, y=400)

                    # name entry box to collect user's name
                    name_entry = tk.Entry(self, width=20, font=(font_type, 12))
                    name_entry.place(x=190, y=400)

                    # phone num label as phoneno_label
                    phoneno_label = tk.Label(self, text="Phone No.: ", font=(font_type, 12, 'bold'))
                    phoneno_label.place(x=85, y=430)

                    # phone num entry box to collect user's phone number
                    phoneno_entry = tk.Entry(self, width=20, font=(font_type, 12))
                    phoneno_entry.place(x=190, y=430)

                    # building in a list to be put inside OptionMenu
                    # bind_func is the function to bind buidling_dropdown and floor_dropdown
                    building = ['Select Building / Block here', 'Block A', 'Block B', 'Block C', 'Block CA', 'Block D', 'Block E', 'Block G']
                    selected_building = tk.StringVar()
                    building_dropdown = ttk.OptionMenu(self, selected_building, *building, command=bind_func)
                    building_dropdown.place(x=190, y=455)

                    # Floor in dict with building as Key, floor_dropdown as values
                    floor = {
                             "Block A": ["-", "Ground Floor", "First Floor", "Second Floor", "Fourth Floor", "Fifth Floor"],
                             "Block B": ["-", "First Floor", "Second Floor", "Fifth Floor"],
                             "Block C": ["-", "Ground Floor", "First Floor", "Second Floor", "Third Floor"],
                             "Block CA": ["-", "Ground Floor", "First Floor", "Second Floor"],
                             "Block D": ["-", "Ground Floor"],
                             "Block E": ["-", "Ground Floor", "Tenth Floor"],
                             "Block G": ["-", "LG2", "Level G", "Level 1", "Level 8", "Level 9", "Level 10", "Level 11"]
                             }
                    selected_floor = tk.StringVar()
                    
                    # Floor Dropdown that binds with building dropdown
                    floor_dropdown = ttk.OptionMenu(self, selected_floor, '-')
                    floor_dropdown.place(x=190, y=480)
                    
                    # Send button that will print user to print_text()
                    send_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Send", width="8", height=5,
                                            bg="#32de97", command=print_text)
                    send_button.place(x=6, y=401, height=90)

                # make food_dict as dict
                new_food_dict = dict(food_dict)

                if food in new_food_dict:
                    convo_log.config(state=tk.NORMAL)
                    food_price_delivery = food_dict.get(food)
                    food_price = food_price_delivery[0]
                    delivery_service = food_price_delivery[1]
                    convo_log.insert(tk.END, "Bot: The price is RM" + str(food_price) + "\nDelivery Services: "
                                     + delivery_service)
                    convo_log.see(tk.END)
                    convo_log.config(state=tk.DISABLED)

                    #  User get to choose between self pickup or delivery here
                    if delivery_service == 'yes':

                        convo_log.config(state=tk.NORMAL)
                        convo_log.insert(tk.END, "\nBot: Self Pick Up or require delivery service")
                        convo_log.see(tk.END)
                        convo_log.config(state=tk.DISABLED)

                        # self pickup button
                        self_pickup_button = tk.Button(self, text="Self Pick Up", font=(font_type, 14),
                                                       bg=btn_colour)
                        self_pickup_button.place(x=76, y=401, height=70)

                        # delivery button
                        delivery_button = tk.Button(self, text="Delivery Service", font=(font_type, 14),
                                                    bg=btn_colour, command=delivery_services)
                        delivery_button.place(x=216, y=401, height=70)

                        # lambda is used to here as the function is outside of this function
                        self_pickup_button['command'] = lambda self_pickup_btn = self_pickup_button, delivery_btn = \
                            delivery_button: delivery_yes_delete(self_pickup_btn, delivery_btn)

                    if delivery_service == 'no':
                        convo_log.config(state=tk.NORMAL)
                        convo_log.insert(tk.END, "\n\nBot: This item does not provide delivery service"
                                                 "\nYou must visit the restaurant to pick up the item."
                                                 "\nPress [Yes] if you wish to proceed to self pick up"
                                                 "\n[Menu] if you wish to change item,"
                                                 "\n[Stall Selection] if you wish to go back to\nStall Selection page.")
                        convo_log.see(tk.END)
                        convo_log.config(state=tk.DISABLED)

                        # Yes button indicate user proceed with self pickup
                        # menu button indicate user wish to change item
                        # stall button indicate user wish to go back to stall selection
                        yes_button = tk.Button(self, text='Yes', font=(font_type, 14), bg=btn_colour)
                        yes_button.place(x=86, y=401, height=50)
                        menu_button = tk.Button(self, text='Menu', font=(font_type, 14), bg=btn_colour)
                        stall_select_button = tk.Button(self, text='Stall Selection', font=(font_type, 14), bg=btn_colour)
                        menu_button.place(x=156, y=401, height=50)
                        stall_select_button.place(x=246, y=401, height=50)

                        # buttons command here and lambda is used as function is outside of this function
                        yes_button['command'] = lambda yes_btn=yes_button, menu_btn=menu_button, stall_select_btn = stall_select_button: \
                            self_pickup_click_delete(yes_btn, menu_btn, stall_select_btn)
                        menu_button['command'] = lambda yes_btn = yes_button, menu_btn = menu_button, stall_select_btn = stall_select_button: \
                            menu_click_delete(yes_btn, menu_btn, stall_select_btn)
                        stall_select_button['command'] = lambda yes_btn = yes_button, menu_btn = menu_button, stall_select_btn = stall_select_button:\
                            stall_click_delete(yes_btn, menu_btn, stall_select_btn)
                        convo_log.config(state=tk.DISABLED)

            # Food is listed using OptionMenu function
            selected_item = tk.StringVar()
            selected_item.set("Select Your Food Here")
            dropdown_menu = tk.OptionMenu(self, selected_item, *list_menu)
            dropdown_menu.configure(font=(font_type, 12), width=30)
            dropdown_menu.place(x=80, y=401)

            # submit button
            submit_button = tk.Button(self, text='submit', font=(font_type, 12), bd='2 pixels', relief='raised', command=print_to_convowindow)
            submit_button.place(x=150, y=451)

            # Back Button
            back_button = tk.Button(self, text='Back', font=(font_type, 12), bd='2 pixels', relief='raised', command=back)
            back_button.place(x=220, y=451)

        # Create window
        self.geometry("450x525")
        self.resizable(width=False, height=False)
        icon = tk.PhotoImage(file='chatbot_icon.png')
        self.iconphoto(True, icon)
        self.title('Food Ordering Chatbot')

        # Conversation window
        convo_log = tk.Text(self, bd=0, bg=bg_colour, height='10', width='60')
        convo_log.place(x=6, y=6, height=386, width=420)

        # Scroll bar
        scrollbar = tk.Scrollbar(self, command=convo_log.yview, cursor="arrow")
        convo_log['yscrollcommand'] = scrollbar.set
        scrollbar.place(x=430, y=6, height=386)

        def stall_selection():
            """Perform data retrieval from dataset.py in respective function
             """

            def button_destroy():
                """to destroy buttons in stall_selection()
                """
                mamak_button.destroy()
                beverage_button.destroy()
                korean_button.destroy()
                japanese_button.destroy()
                malay_button.destroy()

            def malay_stall():

                item_name, list_menu, food_price, delivery_service = ds.malay_data()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Malay Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                convo_log.see(tk.END)  # to view the latest message that is printed onto the convo_log screen
                button_destroy()
                dropdown(ds.to_dict(list_menu, food_price, delivery_service), list_menu)

            def mamak_stall():

                item_name, list_menu, food_price, delivery_service = ds.mamak_data()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Mamak Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                convo_log.see(tk.END)
                button_destroy()
                dropdown(ds.to_dict(list_menu, food_price, delivery_service), list_menu)

            def beverage_stall():

                item_name, list_menu, food_price, delivery_service = ds.beverages_data()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Beverage Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                convo_log.see(tk.END)
                button_destroy()
                dropdown(ds.to_dict(list_menu, food_price, delivery_service), list_menu)

            def korean_stall():

                item_name, list_menu, food_price, delivery_service = ds.korean_data()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Korean Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                convo_log.see(tk.END)
                button_destroy()
                dropdown(ds.to_dict(list_menu, food_price, delivery_service), list_menu)

            def japanese_stall():

                item_name, list_menu, food_price, delivery_service = ds.japanese_data()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Japanese Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                convo_log.see(tk.END)
                button_destroy()
                dropdown(ds.to_dict(list_menu, food_price, delivery_service), list_menu)

            # Malay Button
            malay_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Malay", width="9", height='5',
                                     bg=btn_colour, command=malay_stall)
            malay_button.place(x=6, y=401, height=90)

            # Mamak Button
            mamak_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Mamak", width="9", height='5',
                                     bg=btn_colour, command=mamak_stall)
            mamak_button.place(x=90, y=401, height=90)

            # Beverage Button
            beverage_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Beverage", width="9", height='5',
                                        bg=btn_colour, command=beverage_stall)
            beverage_button.place(x=175, y=401, height=90)

            # Korean Button
            korean_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Korean", width="9", height='5',
                                      bg=btn_colour, command=korean_stall)
            korean_button.place(x=260, y=401, height=90)

            # Japanese Button
            japanese_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Japanese", width="9", height='5',
                                        bg=btn_colour, command=japanese_stall)
            japanese_button.place(x=345, y=401, height=90)

            # first message by chatbot
            convo_log.config(state=tk.NORMAL)
            convo_log.insert(tk.END, "\nBot: " + to_show)
            convo_log.config(state=tk.DISABLED, font=('Arial', 14))
            convo_log.see(tk.END)

        stall_selection()


chatbotapp = Application()  # to run the Application class as chatbotapp
chatbotapp.mainloop()
