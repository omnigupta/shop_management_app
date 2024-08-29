import time
# Reading the Inventory
fd=open("Inventory.txt",'r')
products=fd.read().split('\n')
fd.close()

#Taling user input
ui_username = input("Enter name:")
ui_phone = input("Enter Phone No:")
if ui_phone.isdigit() and len(ui_phone) == 10:  # Assuming a 10-digit phone number
    print(f"Phone number entered: {ui_phone}")
else:
    print("Invalid phone number. Please enter a 10-digit number.")
ui_email = input("Enter Email:")
ui_prod_id = input("Enter Product Id:")
ui_prod_qn = input("Enter Product Quantity:")

updated_prod_lst = []

#Going through each product detail
for product in products:
    prod_details = product.split(',') 
    if(prod_details[0]==ui_prod_id):
    #checking if product exits or not
        if(int(ui_prod_qn) <= int(prod_details[3])):
        #Checking if we are having enough quantity 
            print("-----------------------------")
            print("Product Name           :", prod_details[1])
            print("Price                  :", prod_details[2])
            print("Quantity               :", ui_prod_qn)
            print("-----------------------------")
            print("Billing Amount         :", int(prod_details[2])*int(ui_prod_qn))
            print("-----------------------------")
            #Updating inventory list
            prod_details[3] = str(int(prod_details[3]) - int(ui_prod_qn))

            fd=open("Sales.txt","a")
            sales_detail = ui_username + ',' + ui_phone + ',' + ui_email + ',' + prod_details[1] + ',' + ui_prod_id + ',' + ui_prod_qn + ',' + str(int(prod_details[2])*int(ui_prod_qn)) + ',' + time.ctime()+'\n'
            fd.write(sales_detail)
            fd.close()

        else:
        #if we are not having enough quantity 
            print("Sorry, We're not having enough quanity of product in our Inventory.")
            print("We're only having " + str(prod_details[3]) + " quantity.")
            print("Would you like to purchase it?")
    
            ch = input("Press Y/N: ")
            if(ch == "Y" or ch == 'y'):
            #if you want to purchase with remaining quantity
                print("-----------------------------")
                print("Product Name           :", prod_details[1])
                print("Price                  :", prod_details[2])
                print("Quantity               :", prod_details[3])
                print("-----------------------------")
                print("Billing Amount         :", int(prod_details[2])*int(prod_details[3]))
                print("-----------------------------")
            
                #Generating Sales in Sales.txt
                fd=open("Sales.txt","a")
                sales_detail = ui_username + ',' + ui_phone + ',' + ui_email + ',' + prod_details[1] + ',' + ui_prod_id + ',' + prod_details[3] + ',' + str(int(prod_details[2])*int(prod_details[3])) + ',' + time.ctime()+'\n'
                fd.write(sales_detail)
                fd.close()
                
                #Updating Inventory list
                prod_details[3] = '0'

            else:
                print('Thank you')
                
    #Updating my Inventory list
    updated_prod_lst.append(prod_details)
    
lst =[]
#Updating my Inventory string
for i in updated_prod_lst:
    prod = i[0] + "," + i[1] + "," + i[2] + "," + i[3] + '\n'
    lst.append(prod)
#Removing last '\n' from the list    
lst[-1] = lst[-1][:-1]
#Updating my Inventory file
fd= open('Inventory.txt','w')

for i in lst:
    fd.write(i)
    
fd.close() 

print("-----------------------------")
print("Inventory Update")