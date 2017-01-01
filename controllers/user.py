from gluon.storage import Storage


def login():
   import time
   form = FORM('Username',INPUT(_name='username', requires=[IS_NOT_EMPTY()]),
                'Password',INPUT(_name='password',_type='password' ,requires=[IS_NOT_EMPTY()]),
                INPUT(_type='submit',_value='Submit'))
   username = request.vars.username
   password = request.vars.password
   rows = db( (db.user.Username == username) & (db.user.Password==password)).select()
   rows2 = db((db.role.Username == username)).select()
   if (form.process().accepted):
    # session.flash = "Wrong username or password"
     #redirect(URL('user','login'))
     if len(rows)==0:
         response.flash = "Wrong username or password"


     else:
         session.user = rows[0]
         session.role = rows2[0]
         print rows
         print rows2
         return redirect(URL('default','index'))

   return dict(form=form,page_title="Login Screen")

def logout():
    global user
    user = None
    session.user = None
    session.role=None
    return redirect(URL('default','index'))

def register():
     form = SQLFORM(db.user).process()
     if form.accepted:
                db.role.insert(Username = form.vars.Username)

     return dict(form = form,page_title="Register");
def edit():
    return dict(page_title='Edit')
