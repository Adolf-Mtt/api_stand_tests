# This is a sample Python script.
import sender_stand_request
import data
import create_user_test

if __name__ == '__main__':
    #pass

#    rsp1 = sender_stand_request.get_users_table()
#    rsp = create_user_test.test_create_user_15_letter_in_first_name_get_success_response()
    rsp1 = sender_stand_request.get_logs()
    print('main')
    print(rsp1)
    print('Json && text')
    print(rsp1.text)
    # print(rsp.status_code)
    # print(rsp.text)