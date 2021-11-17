import tkinter as tk
import pandas as pd

df = pd.read_csv('Food List.csv')
menu = ['Malay', 'Mamak', 'Beverage', 'Korean', 'Japanese']
to_show = "Hello! Welcome to Food Ordering Chatbot! Please type out the stall name first: \n 1. {0}\n 2. {1}\n " \
          "3. {2}\n 4. {3}\n 5. {4}\n\n".format(*menu)
name = address = None
item_price = []
item_cart = []
cart = {name: [address, item_cart, item_price]}


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        bg_colour = '#feffe0'
        font_type = 'Calibri'
        global df
        global to_show
        global name, item_price, address, item_cart, cart
        stall_btn_colour = '#e3a28d'

        def dropdown(food_dict, list_menu):
            """
            dropdown function is to display menu selection
            to the user with tk.OptionMenu method from tkinter library.
            This function is a nested function.
            food_dict is a dictionary created in stall_selection()
            list_menu is a list created in stall_selection()
            """
            def update_cart(name, address, item_cart, item_price):
                del cart[None]
                cart[name] = [address, item_cart, item_price]
                return cart

            def print_to_convowindow():
                convo_log.config(state=tk.NORMAL)
                food = selected_item.get()
                convo_log.insert(tk.END, "You: " + food + '\n\n')
                convo_log.config(state=tk.DISABLED)
                dropdown_menu.destroy()
                submit_button.destroy()
                chatbot_application(food)

            def chatbot_application(food):
                """
                chatbot_application function is to carry out chatbot application such as:
                delivery services, self pickup, and provide name and address to have delivery services
                this function is a nested function as each chatbot application is in function
                food parameter is used to determine the price and the availability of the item
                """
                def exit_program(stl_btn, chk_btn):
                    stl_btn.destroy()
                    chk_btn.destroy()
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "You: Exit\n\nBot: Goodbye and see you again.")
                    self.quit()

                def click_delete(stl_btn, chk_btn):
                    item_price.clear()
                    item_cart.clear()
                    stall_selection()
                    stl_btn.destroy()
                    chk_btn.destroy()

                def self_pickup_click_delete(yes_btn, menu_btn, stall_select_btn):
                    item_price.append(food_price)
                    item_cart.append(food)
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Self Pick Up")
                    self_pickup()
                    convo_log.config(state=tk.DISABLED)
                    yes_btn.destroy()
                    menu_btn.destroy()
                    stall_select_btn.destroy()

                def menu_click_delete(yes_btn, menu_btn, stall_select_btn):
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Menu")
                    convo_log.config(state=tk.DISABLED)
                    yes_btn.destroy()
                    menu_btn.destroy()
                    stall_select_btn.destroy()
                    dropdown(food_dict, list_menu)

                def stall_click_delete(yes_btn, menu_btn, stall_select_btn):
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Stall Selection")
                    convo_log.config(state=tk.DISABLED)
                    yes_btn.destroy()
                    menu_btn.destroy()
                    stall_select_btn.destroy()
                    stall_selection()

                def delivery_yes_delete(self_pickup_btn, delivery_btn):
                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Self Pick Up\n\n")
                    self_pickup_btn.destroy()
                    delivery_btn.destroy()
                    self_pickup()

                def checkout_click_delete(chk_stl_btn, chk_chk_btn):
                    stall_selection()
                    chk_chk_btn.destroy()
                    chk_stl_btn.destroy()

                def delivery_click_delete(del_stl_btn, del_chk_btn):
                    del_stl_btn.destroy()
                    del_chk_btn.destroy()
                    stall_selection()

                def self_pickup():
                    """
                    self_pickup function is to carry out self pickup application.
                    This function will be the end of each order, if user wish to order food again,
                    users will have to select stall_btn to reach stall selection page which is stall_selection()
                    """

                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nBot: You have ordered " + food +
                                     '\nand the total price is RM' + str(food_price) +
                                     '\n\nBot: Ordered Successful, please pay at counter\n\n'
                                     'Bot: Do you wish to order food again? '
                                     '\nPress [stall selection] to view the stall,'
                                     '\n[Exit] to quit\n\n')
                    convo_log.config(state=tk.DISABLED)
                    exit_btn = tk.Button(self, text="Exit", font=(font_type, 14),
                                         bg=stall_btn_colour)
                    stall_btn = tk.Button(self, text="Stall Selection", font=(font_type, 14),
                                          bg=stall_btn_colour)
                    stall_btn['command'] = lambda stl_btn=stall_btn, chk_btn=exit_btn: click_delete(stl_btn, chk_btn)
                    exit_btn.place(x=250, y=401, height=50)
                    exit_btn['command'] = lambda stl_btn=stall_btn, chk_btn=exit_btn: exit_program(stl_btn, chk_btn)
                    stall_btn.place(x=80, y=401, height=50)

                def delivery_services():
                    """
                    delivery_service function is to carry out delivery application.
                    This function is a nested function as it consists of printing text to conversation window,
                    checkout function.
                    This function is used to record user's information (address and name) to have the delivery services
                    user have the chance to order food again and store in cart(dictionary).
                    """

                    def print_text():

                        def checkout(user_name, user_address):
                            delivery_checkout_btn.destroy()
                            delivery_stall_btn.destroy()
                            name = user_name
                            address = user_address
                            convo_log.config(state=tk.NORMAL)
                            convo_log.insert(tk.END, "\n\nYou: Check Out")
                            order_cart = update_cart(name, address, item_cart, item_price)
                            values = order_cart[name]
                            price = values[2]
                            total_price = 0
                            for j in price:
                                total_price += j
                            item = '\n'.join([str(i) for i in item_cart])
                            convo_log.insert(tk.END,"\n\nBot: You have successfully ordered " + item
                                             + "\ntotal price is: RM"
                                             + str(total_price))
                            convo_log.insert(tk.END, '\n\nBot: Do you wish to order food again? '
                                             '\nPress [stall selection] to view the stall,'
                                             '\n[Exit] to quit')
                            chkout_exit_btn = tk.Button(self, text="Exit", font=(font_type, 14), bg=stall_btn_colour)
                            chkout_exit_btn.place(x=250, y=401, height=50)
                            chkout_stall_button = tk.Button(self, text="Stall Selection", font=(font_type, 14), bg=stall_btn_colour)
                            chkout_stall_button.place(x=80, y=401, height=50)
                            chkout_stall_button['command'] = lambda chk_stl_btn=chkout_stall_button, chk_chk_btn=chkout_exit_btn: checkout_click_delete(chk_stl_btn, chk_chk_btn)
                            chkout_exit_btn['command'] = lambda chk_stl_btn=chkout_stall_button, chk_chk_btn=chkout_exit_btn: exit_program(chk_stl_btn, chk_chk_btn)

                        user_address = address_entry.get("1.0", tk.END + "-1c").strip()
                        user_name = name_entry.get("1.0", tk.END + "-1c")
                        if user_name and user_address != '':

                            convo_log.config(state=tk.NORMAL)
                            convo_log.insert(tk.END, "\n\nYou: \n" + user_name + '\n' + user_address + '\n\n' +
                                             "Bot: Do you wish to proceed to checkout or go back to stall selection "
                                             "to choose other food")
                            address_entry.destroy()
                            name_entry.destroy()
                            name_label.destroy()
                            address_label.destroy()
                            send_button.destroy()
                            delivery_checkout_btn = tk.Button(self, text="Checkout", font=(font_type, 14), bg=stall_btn_colour)
                            delivery_stall_btn = tk.Button(self, text="Stall Selection", font=(font_type, 14), bg=stall_btn_colour)
                            delivery_stall_btn['command'] = lambda del_stl_btn=delivery_stall_btn, del_chk_btn=delivery_checkout_btn: delivery_click_delete(del_stl_btn, del_chk_btn)
                            delivery_checkout_btn.place(x=250, y=401, height=50)
                            delivery_checkout_btn['command'] = lambda username=user_name, useraddress=user_address: checkout(username, useraddress)
                            delivery_stall_btn.place(x=80, y=401, height=50)

                        else:
                            convo_log.config(state=tk.NORMAL)
                            convo_log.insert(tk.END, "\n\nBot: Please enter your name and address then     press send")

                    convo_log.config(state=tk.NORMAL)
                    convo_log.insert(tk.END, "\n\nYou: Delivery Service\n\n"
                                             "Bot: Please enter Your name and address in this   format: \n"
                                             "xxx[Floor][,][Building]\nxxx[Street name][,][House number]\n"
                                             "xxx[City or Taman]\nxxx[Postcode][,][City]\nxxx[State]")

                    convo_log.config(state=tk.DISABLED)
                    delivery_button.destroy()
                    self_pickup_button.destroy()
                    name_label = tk.Label(self, text="Name: ", font=(font_type, 12, 'bold'))
                    address_label = tk.Label(self, text="Address: ", font=(font_type, 12, 'bold'))
                    name_label.place(x=85, y=400)
                    address_label.place(x=85, y=431)
                    name_entry = tk.Text(self, width=30, font=(font_type, 12))
                    name_entry.place(x=155, y=400, height=23)
                    address_entry = tk.Text(self, width=30, font=(font_type, 12))
                    address_entry.place(x=155, y=431, height=55)
                    send_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Send", width="8", height=5,
                                            bg="#32de97", command=print_text)
                    send_button.place(x=6, y=401, height=90)

                new_food_dict = dict(food_dict)
                if food in new_food_dict:
                    convo_log.config(state=tk.NORMAL)
                    food_price_delivery = food_dict.get(food)
                    food_price = food_price_delivery[0]
                    delivery_service = food_price_delivery[1]
                    convo_log.insert(tk.END, "Bot: The price is RM" + str(food_price) + "\nDelivery Services: "
                                     + delivery_service)
                    if delivery_service == 'yes':
                        item_price.append(food_price)
                        item_cart.append(food)
                        convo_log.insert(tk.END, "\nBot: Self Pick Up or require delivery service")
                        self_pickup_button = tk.Button(self, text="Self Pick Up", font=(font_type, 14),
                                                       bg=stall_btn_colour, command=self_pickup)
                        self_pickup_button.place(x=76, y=401, height=70)
                        delivery_button = tk.Button(self, text="Delivery Service", font=(font_type, 14),
                                                    bg=stall_btn_colour, command=delivery_services)
                        delivery_button.place(x=216, y=401, height=70)
                        self_pickup_button['command'] = lambda self_pickup_btn = self_pickup_button, delivery_btn = delivery_button: delivery_yes_delete(self_pickup_btn, delivery_btn)
                    if delivery_service == 'no':
                        convo_log.insert(tk.END, "\n\nBot: This item does not provide delivery service"
                                                 "\nYou must visit the restaurant to pick up the item."
                                                 "\nPress [Yes] if you wish to proceed to self pick up"
                                                 "\n[Menu] if you wish to change item,"
                                                 "\n[Stall Selection] if you wish to go back to \t\tStall Selection page.")
                        yes_button = tk.Button(self, text='Yes', font=(font_type, 14), bg=stall_btn_colour)
                        yes_button.place(x=86, y=401, height=50)
                        menu_button = tk.Button(self, text='Menu', font=(font_type, 14), bg=stall_btn_colour)
                        stall_select_button = tk.Button(self, text='Stall Selection', font=(font_type, 14),
                                                        bg=stall_btn_colour)
                        menu_button.place(x=156, y=401, height=50)
                        stall_select_button.place(x=246, y=401, height=50)
                        yes_button['command'] = lambda yes_btn=yes_button, menu_btn=menu_button, stall_select_btn = stall_select_button: \
                            self_pickup_click_delete(yes_btn, menu_btn, stall_select_btn)
                        menu_button['command'] = lambda yes_btn = yes_button, menu_btn = menu_button, stall_select_btn = stall_select_button: \
                            menu_click_delete(yes_btn, menu_btn, stall_select_btn)
                        stall_select_button['command'] = lambda yes_btn = yes_button, menu_btn = menu_button, stall_select_btn = stall_select_button:\
                            stall_click_delete(yes_btn, menu_btn, stall_select_btn)
                        convo_log.config(state=tk.DISABLED)

            selected_item = tk.StringVar()
            selected_item.set("Select Your Food Here")
            dropdown_menu = tk.OptionMenu(self, selected_item, *list_menu)
            dropdown_menu.configure(font=(font_type, 12), width=30)
            dropdown_menu.place(x=80, y=401)

            # submit button
            submit_button = tk.Button(self, text='submit', font=(font_type, 12), bd='2 pixels', relief='raised', command=print_to_convowindow)
            submit_button.place(x=180, y=451)

        # Create window
        window = tk.Frame(self)
        self.geometry("450x500")
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

        def to_dict(list_menu, food_price, delivery_service):
            zipfile = zip(list_menu, food_price, delivery_service)
            food_dict = {}
            for i, j, k in zipfile:
                food_dict[i] = [j, k]
            return food_dict

        def stall_selection():
            """
            stall_selection () is used to convert the user's selection into dictionary and list

            """

            def button_destroy():
                """
                to destroy buttons created in Application.__init__()
                """
                mamak_button.destroy()
                beverage_button.destroy()
                korean_button.destroy()
                japanese_button.destroy()
                malay_button.destroy()

            def malay_stall():
                item_name = df['item_name'][0:13].to_string()
                list_menu = df['item_name'][0:13].tolist()
                food_price = df['price'][0:13].tolist()
                delivery_service = df['delivery_service'][0:13].tolist()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Malay Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                button_destroy()
                dropdown(to_dict(list_menu, food_price, delivery_service), list_menu)

            def mamak_stall():
                item_name = df['item_name'][13:32].to_string()
                list_menu = df['item_name'][13:32].tolist()
                food_price = df['price'][13:32].tolist()
                delivery_service = df['delivery_service'][13:32].tolist()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Mamak Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                button_destroy()
                dropdown(to_dict(list_menu, food_price, delivery_service), list_menu)

            def beverage_stall():
                item_name = df['item_name'][32:47].to_string()
                list_menu = df['item_name'][32:47].tolist()
                food_price = df['price'][32:47].tolist()
                delivery_service = df['delivery_service'][32:47].tolist()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Beverage Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                button_destroy()
                dropdown(to_dict(list_menu, food_price, delivery_service), list_menu)

            def korean_stall():
                item_name = df['item_name'][47:62].to_string()
                list_menu = df['item_name'][47:62].tolist()
                food_price = df['price'][47:62].tolist()
                delivery_service = df['delivery_service'][47:62].tolist()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Korean Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                button_destroy()
                dropdown(to_dict(list_menu, food_price, delivery_service), list_menu)

            def japanese_stall():
                item_name = df['item_name'][62:87].to_string()
                list_menu = df['item_name'][62:87].tolist()
                food_price = df['price'][62:87].tolist()
                delivery_service = df['delivery_service'][62:87].tolist()
                convo_log.config(state=tk.NORMAL)
                convo_log.insert(tk.END, "You: Japanese Stall\n\n")
                convo_log.insert(tk.END, "Bot: The items are as follows:\n\n" + str(item_name) + "\n\n")
                convo_log.config(state=tk.DISABLED)
                button_destroy()
                dropdown(to_dict(list_menu, food_price, delivery_service), list_menu)

            # Malay Button
            malay_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Malay", width="9", height='5', bg=stall_btn_colour, command=malay_stall)
            malay_button.place(x=6, y=401, height=90)

            # Mamak Button
            mamak_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Mamak", width="9", height='5', bg=stall_btn_colour, command=mamak_stall)
            mamak_button.place(x=90, y=401, height=90)

            # Beverage Button
            beverage_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Beverage", width="9", height='5', bg=stall_btn_colour, command=beverage_stall)
            beverage_button.place(x=175, y=401, height=90)

            # Korean Button
            korean_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Korean", width="9", height='5', bg=stall_btn_colour, command=korean_stall)
            korean_button.place(x=260, y=401, height=90)

            # Japanese Button
            japanese_button = tk.Button(self, font=(font_type, 12, 'bold'), text="Japanese", width="9", height='5', bg=stall_btn_colour, command=japanese_stall)
            japanese_button.place(x=345, y=401, height=90)

            # first message by chatbot
            convo_log.insert(tk.END, "\nBot: " + to_show)
            convo_log.config(state=tk.DISABLED, font=('Arial', 14))

        stall_selection()


chatbotapp = Application()
chatbotapp.mainloop()
