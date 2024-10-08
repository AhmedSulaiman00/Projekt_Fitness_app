import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database = "fitlife_workout_app_db",
    ssl_disabled = True
)

cursor = mydb.cursor()

wkUser_name = ""
wkUser_id = 0

#Simple login proccess
def wkLogin():
    wkloggedIn = False
    while wkloggedIn == False:
        wkUser_name = input("What is your username?")
        query = """
            SELECT ID FROM benutzer
            WHERE Vorname = %s
        """
        values = (wkUser_name,)
        cursor.execute(query, values)
        wkResults = cursor.fetchone()
        if isinstance(wkResults, tuple) == True:
            for i in wkResults:
                global wkUser_id
                wkUser_id = i
            wkloggedIn = True
            print("\nYou are logged in!\n")
        else:
            print("\nThis user does not exist! \nTry again, or create an account\n")

#Function to close the app (main function)
def wkApp_closing(boolean):
    wkApp_close_input = input("Would you like to close the app? (y/n)")
    if wkApp_close_input == "y": boolean = True; print("\nSuccessfully closed the app!\n")
    return boolean

def create_übung_get_übungID() -> int:
    # Create the Übung
    wkExercise_name = input("What is the name of the exercise?\t")
    query = """
    INSERT INTO übung(Name)
    SELECT %s
    WHERE NOT EXISTS (
        SELECT 1 FROM übung WHERE Name = %s
    );
    """
    values = (wkExercise_name, wkExercise_name)
    cursor.execute(query, values)
    mydb.commit()

    # Get the übung id
    query = """
    SELECT ID FROM Übung
    WHERE Name = %s
    """
    values = (wkExercise_name,)
    cursor.execute(query, values)
    wkResults = cursor.fetchone()
    if isinstance(wkResults, tuple) == True:
        for i in wkResults:
            return i 


def create_wk_get_wkID() -> int:
    # Create the workout
    datum = input("Enter the date in this format: \"YYYY-MM-DD\"\t")
    wkWorkout_type = input("What is the type of workout? (e.g. Pull, Push)\t")
    query = """
    INSERT INTO workout(Benutzer_ID, Workout_typ, Datum)
    VALUES(%s, %s, %s);
    """
    values = (wkUser_id ,wkWorkout_type, datum)
    cursor.execute(query, values)
    mydb.commit()

    # Get the workout id
    query = """
    SELECT ID FROM workout
    WHERE Benutzer_ID = %s
    AND Datum = %s
    """
    values = (wkUser_id, datum)
    cursor.execute(query, values)
    wkResults = cursor.fetchone()
    if isinstance(wkResults, tuple) == True:
        for i in wkResults:
            return i 

#function to add a workout
def wkAdding_workout():
    wkFinish = False
    wkWorkout_id = create_wk_get_wkID()
    while wkFinish == False:
        wkNew_exercise = input("add new excercise? (y/n)\t")
        if wkNew_exercise == "y":
            wkÜbung_id = create_übung_get_übungID()
            wkExercise_results_dict = {
                "Wiederholungen" : [],
                "Gewicht": [],
                "Schwierigkeit" : []
            }
            counter = 0
            while True:
                counter += 1
                wkExercise_Gewicht = input("What is the weight of the current set\t")
                Wiederholungen = input("How many reps did you do this set\t")
                wkExercise_difficulty = input("How difficult was this set? Rate in percent (e.g. 60%)\t")
                wkAnother_one = input("Do you want to add a new set? (y/n)\t")

                wkExercise_results_dict["Gewicht"].append(wkExercise_Gewicht)
                wkExercise_results_dict["Wiederholungen"].append(Wiederholungen)
                wkExercise_results_dict["Schwierigkeit"].append(wkExercise_difficulty)
                if wkAnother_one == "n": 
                    i = 0
                    while i < counter:
                        liste_werte = []
                        for key in wkExercise_results_dict:
                            liste_werte.append(wkExercise_results_dict[key][i])
                        query = """
                        INSERT INTO satz(Workout_ID, Übung_ID, Set_NR, Wiederholungen, Gewicht, Schwierigkeit)
                        VALUES(%s, %s, %s, %s, %s, %s)
                        """
                        values = (wkWorkout_id, wkÜbung_id, (i+1), liste_werte[0], liste_werte[1], liste_werte[2])
                        cursor.execute(query, values)
                        i += 1
                        if i == counter:
                            mydb.commit()
                    finish_Workout = input("do you want to finish the workout? (y/n)")
                    if finish_Workout == "y":
                        print("workout finished")
                        wkFinish = True
                        break
                    else:
                        break
        else:
            wkCancel = input("do you want to cancel the workout? (y/n)\t")
            if wkCancel == "y":
                wkFinish = True

wkLogin()
wkClose_app = False
while (wkClose_app == False):
    wkNew_workout = input("Do you want to add a new workout? (y/n)")
    if wkNew_workout == "y":
        wkAdding_workout()
        wkNew_workout = ""
    wkClose_app = wkApp_closing(wkClose_app)


cursor.close()
mydb.close()