import kivy
import csv
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout


class Add_Item(BoxLayout):
    pass

class Item(GridLayout):
    pass



#Check if there is file with list
#parse list
#app manager class

class FileManager():
    #DOES creating/locating, reading, editing list file
    list_data = []
    def __init__(self, **kwargs): 

        #ran at start up to make sure there is a list file
        #if not, creates a new one
        #if present, proceeds to load info from file
        try :
            with open('list.csv',newline='') as listfile:
                print('File found')
                
                data = csv.reader(listfile)
                for item in data:
                    print(item)
                    self.list_data.append(item)

            return

            
        except Exception:
            print('An error occured .File not present! Creating new list file.')
            return
            #TODO
            return
        
    def file_add(self,new_item):
        print("Adding to file")
        print(new_item)
        new_item = [new_item]
        print(new_item)

        
        with open('list.csv','a',newline='') as listfile:
            
            f = csv.writer(listfile)

            f.writerow(new_item)

            

        with open('list.csv','r',newline='') as listfile:
            data = csv.reader(listfile)
            
            new_list =[]
             
            for item in data:
                    print(item)
                    new_list.append(item)

        return new_list
        

    def file_remove(self):
        lines = []

        with open('list.csv','r',newline='') as listfile:
            data = csv.reader(listfile)
            
            for item in data:
                    print(item)
                    lines.append(item)

        if not lines:
            return

        lines.pop(len(lines)-1)
        print(lines)

        with open('list.csv','w',newline='') as listfile:
            f = csv.writer(listfile)

            f.writerows(lines)
     
        new_list = []
        with open('list.csv','r',newline='') as listfile:
            data = csv.reader(listfile)

            for item in data:
                    print(item)
                    new_list.append(item)

        return new_list

    
    #TODO



class AppBoxLayout(BoxLayout, FileManager):

    
        #call function in file manager
        #app reads and adds tasks on start up
    main_list = []

    def populate(self,data):#responsible for adding to screen
        if self.ids.item_container.children: #if there are items in the container, clear them
            self.ids.item_container.clear_widgets()

        for list_item in data:
            #create ite instance
            filled_item = Item()
            #changes label of widget
            if not list_item[0]:
                continue
            filled_item.ids.ItemLabel.text = list_item[0]
            #adds widget to grid
            self.ids.item_container.add_widget(filled_item)
            

        



    def add_item(self,method,entry):
        #TODO
        #each function only alters the list file
        #once file is altered in the respective FILE MANAGER method,
        #the file manager will read and return a new list  from the file
        #the populate method is then called which clears and re-adds widgets
        #thus updating the list without messing with widgets again

        print("adding")
        
        if method == 0:
            add = Add_Item()
            data= []
            #self.populate(data)

            if self.ids.add_container.children :
                return


            self.ids.add_container.size_hint_y = .2 #set the container height to "un-hide it"
            
            self.ids.add_container.add_widget(add) #adds the text entry with buttons

            return

        if method == 1:
            if not entry:
                return

            #for child in self.ids.add_container.add_space.children:
             
             #   print(child)

            print(self.ids.add_container.children)
            
            new_list = self.file_add(entry)
            self.populate(new_list)




        #END OF THE LINE
         
        #STEPS!
        #get new item or 
        #call filemanager file_add() which should return new list from updated
        #file
        #new list is fed into populate which handles the UI update regardless
        #of addition or removal
        #self.populate(data)#currently returns a blank screen since 
                           #data[] is not given anything right now
        
            #TODO

    def cancel_addition(self):
        self.ids.add_container.clear_widgets()
        self.ids.add_container.size_hint_y = None
        self.ids.add_container.height = 0

        

    def remove_item(self):
        #removes last item of the list
        new_list = self.file_remove()

        if not new_list:
            return

        print("remove prod")
        print(new_list)
        self.populate(new_list)

    






class ChecklistApp(App):

    

    def build(self):
        cl = AppBoxLayout()
        #app.locate_file() at initalisaion
        print(cl.list_data)
        cl.main_list = cl.list_data
        cl.populate(cl.main_list)
        
        return cl

if __name__ == '__main__':
    ChecklistApp().run()