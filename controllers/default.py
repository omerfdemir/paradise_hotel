# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import random
def capitalize(title):
   words = title.split()
   words = [word.capitalize() for word in words]
   return " ".join(words)


def about_us():
    return dict(page_title="About Us")
def login():
    return dict(page_title="Login Screen")

all_rooms = {
            1:{ "name":"Classic Suite",
                        "room_type":"1+1",
                        "person":"2",
                        "price":"150$ per Night",
                        "specs":'Wireless Internet, Private Balcony, Fridge, Washing Machine, Hair Dryer, Iron, Dish Machine, Tea Machine, Microwave Oven, LED TV',
                        "photo":"/paradise_hotel/static/images/rooms/classic_suite.jpg"
                        },
            2:{ "name":"Superior Suite",
                        "room_type":"1+1",
                        "person":"3",
                        "price":"200$ per Night",
                        "specs":'Wireless Internet, Private Balcony, Fridge, Washing Machine, Hair Dryer, Iron, Dish Machine, Tea Machine, Microwave Oven, LED TV',
                        "photo":"/paradise_hotel/static/images/rooms/superior_suite.jpg"
                        },
            3:{ "name":"Deluxe Suite",
                        "room_type":"1+1",
                        "person":"4",
                        "price":"250$ per Night",
                        "specs":'Wireless Internet, Private Balcony, Fridge, Washing Machine, Hair Dryer, Iron, Dish Machine, Tea Machine, Microwave Oven, LED TV',
                        "photo":"/paradise_hotel/static/images/rooms/deluxe_suite.jpg"
                        },
            4:{ "name":"Junior Family Suite",
                        "room_type":"2+1",
                        "person":"6",
                        "price":"300$ per Night",
                        "specs":'Air Conditioner, Wireless Fiber Internet, Private Balcony, Fridge, Washing Machine, Hair Dryer, Iron, Dish Machine, Tea Machine, Microwave Oven, LED TV, Jacuzzi ',
                        "photo":"/paradise_hotel/static/images/rooms/junior_family_suite.jpg"
                        },
            5:{ "name":"Family Suite",
                        "room_type":"2+1 Dublex",
                        "person":"6",
                        "price":"400$ per Night",
                        "specs":'Air Conditioner, Wireless Fiber Internet, Private Balcony, Fridge, Washing Machine, Hair Dryer, Iron, Dish Machine, Tea Machine, Microwave Oven, LED TV, Jacuzzi',
                        "photo":"/paradise_hotel/static/images/rooms/family_suite.jpg"
                        },
            6:{ "name":"Deluxe Family Suite",
                        "room_type":"2+1 Dublex",
                        "person":"8",
                        "price":"500$ per Night",
                        "specs":'Air Conditioner, Wireless Fiber Internet, Private Balcony, Fridge, Washing Machine, Hair Dryer, Iron, Dish Machine, Tea Machine, Microwave Oven, LED TV, Jacuzzi',
                        "photo":"/paradise_hotel/static/images/rooms/deluxe_family_suite.jpg"
                        },

}

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())
def room():
        print request.args
        room_id = int(request.args[0])
        room_data = all_rooms[room_id]
        room_price = room_data["price"]
        price_rooms = []
        session.rooms = room_id
        db_connection = db( (db.room_specs.Room_id == room_id)).select()


        for rid, room in all_rooms.items():
            if room["price"] == room_price and rid != room_id:
                room["room_id"] = rid
                price_rooms.append(room)
        form = FORM('Comment',INPUT(_name='comment'),
                    'Score',INPUT(_name='score',requires=IS_IN_SET({1,2,3,4,5,6,7,8,9,10})),
                    INPUT(_type='submit',_value='Submit'))

        rows = db((db.room_specs.Room_id == room_id)).select('Comments','Username')
        sqlstring = "select avg(Score) from room_specs where Room_id = " + str(room_id)
        avg = db.executesql(sqlstring)




        print room_id
        if form.process().accepted:
            db.room_specs.insert(Room_id =room_id ,
                                Comments=form.vars.comment,
                                Score=form.vars.score,
                                User_id=session.user.id,
                                Username=session.user.Username)
            return redirect(request.env.http_referer)

#        form2 = FORM('Check-İn',INPUT(_name='indate',_type='date'),
#                        'Check-Out',INPUT(_name='outdate',_type='date'),
#                        INPUT(_type='submit',_value='Submit'))
#
#        if form2.process().accepted:
#            db.reservation.insert(User_id =session.user.id ,
#                                        Room_id=room_id,
#                                        inDate=form2.vars.indate,
#                                        outDate=form2.vars.outdate,
#                                        )

        #scores = db((db.room_specs.Room_id == room_id)).select('Score')
        #sum_score = 0
        #count = 0
        #list=[]
        #for i in scores:
        #    list.append(i)
        #for i in list:
        #    sum_score += i
        #    count += 1
        #score = (sum_score/count)
        return dict(page_title="Rooms Specs",data=room_data,    price_rooms=price_rooms,form=form,comments=db_connection,rows=rows,avg=avg)



def rooms():
            sqlstring2 = "select max(avg((Score)) from room_specs"
            max_score = 0
            score=0
            room_id=0
            for i in range(0,7):
                sqlstring2  = "select avg(Score) from room_specs where Room_id = " + str(i)
                score = db.executesql(sqlstring2)
                if score>max_score:
                    max_score=score
                    room_id = i
            room_name= db(db.rooms.id == room_id).select('Type')


            last_reserved_room_id=db(db.reservation).select('Room_id').last()
            room_id_2=last_reserved_room_id.Room_id
            room_name_2=db(db.rooms.id==room_id_2).select('Type')
            print room_name_2
            print max_score,room_id,room_name
            return dict(page_title="Rooms",rooms_data=all_rooms.items(),max_score=max_score,room_name=room_name,
            room_name_2=room_name_2)

def account():
    print request.args
    account_id = request.args(1)
    user_id = session.user.id
    #request.args(0)= account_id
    rows3 = db((db.reservation.id)).select('id','User_id','Room_id','inDate','outDate')
    rows2 = db(db.user.Username).select('id','Username','Name','Surname')
    rows = db((db.reservation.User_id==user_id)&(db.rooms.id==db.reservation.Room_id)).select('Type','inDate','outDate')
    return dict(page_title="Account",rows=rows,rows2=rows2,rows3=rows3)
def reservation():
    user_id = session.user.id
    room_id = session.rooms

    form = FORM('Check-in    : ',INPUT(_name='indate',_type='date'),BR(),
                'Check-Out   :  ',INPUT(_name='outdate',_type='date'),BR(),
                INPUT(_type='submit',_value='Submit'))
    if form.process().accepted:
        response.flash = "Reservation accepted.Happy Holiday!"
        db.reservation.insert(User_id =user_id ,
                                Room_id=room_id,
                                inDate=form.vars.indate,
                                outDate=form.vars.outdate,
                                )
    print room_id
    return dict(page_title="Reservation",form=form)




def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    return dict(page_title="Home Page")
def contact():

    if session.user:
        form=SQLFORM(db.contact).process()
    else:
        form=SQLFORM(db.contact).process()
    rows4 = db(db.contact).select()

    return dict(page_title="Contact",form=form,rows4=rows4)


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
