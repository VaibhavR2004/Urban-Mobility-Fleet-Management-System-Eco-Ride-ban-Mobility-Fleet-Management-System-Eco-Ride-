# logs = "alice:hi bob:hello alice:how_are_you bob:good charlie:hey Invalid_case:"

# def Chat_Application(logs):
#     def valid(log):
#         try:
#             user, text = log.split(":",1)
#             if not user or not text:
#                 raise ValueError("Enter username or text")
#             return user
#         except ValueError as e:
#             print(f"{log}->{e}")
#             return None
#     clean_list = list(map(lambda log:valid(log),logs.split()))
#     filtered_list = list(filter(lambda t:t is not None,clean_list))
#     print(filtered_list)
#     # chater_list =list(map(lambda v:v.split(":")[0],logs.split()))
# Chat_Application(logs)

def Chat_Application(logs):

    def valid(log):
        try:
            user, text = log.split(":", 1)
            if not user or not text:
                raise ValueError("Enter username or text")
            return (user, text)
        except ValueError as e:
            print(f"{log} -> {e}")
            return None

    clean_list = list(map(valid, logs.split()))
    filtered_list = list(filter(lambda x: x is not None, clean_list))

    users = list(map(lambda x: x[0], filtered_list))

    unique_users = set(users)


    freq = {}
    for u in users:
        freq[u] = freq.get(u, 0) + 1

    # 🔹 Step 6: Active users
    active_users = list(filter(lambda u: freq[u] > 1, freq))


    conversations = {}
    for user, msg in filtered_list:
        conversations.setdefault(user, []).append(msg)


    print("✅ Filtered List:", filtered_list)
    print("👥 Unique Users:", unique_users)
    print("📊 Frequency:", freq)
    print("🔥 Active Users:", active_users)

    return conversations



def get_user_messages(conversations, username):
    return conversations.get(username, [])


# logs = "alice:hi bob:hello alice:how_are_you bob:good charlie:hey invalid bob: :test"

# data = Chat_Application(logs)

# print(" Alice Messages:", get_user_messages(data, "alice"))
# print("Bob Messages:", get_user_messages(data, "bob"))



class Chat_Agent:
    def __init__(self, logs):
        self.logs = logs
        self.conversations = {}
    
    
    def Chat_Application(self,logs):

        def valid(log):
            try:
                user, text = log.split(":", 1)
                if not user or not text:
                    raise ValueError("Enter username or text")
                return (user, text)
            except ValueError as e:
                print(f"{log} -> {e}")
                return None

        clean_list = list(map(valid, logs.split()))
        filtered_list = list(filter(lambda x: x is not None, clean_list))

        users = list(map(lambda x: x[0], filtered_list))

        unique_users = set(users)


        freq = {}
        for u in users:
            freq[u] = freq.get(u, 0) + 1


        active_users = list(filter(lambda u: freq[u] > 1, freq))


        for user, msg in filtered_list:
            self.conversations.setdefault(user, []).append(msg)


        print("Filtered List:", filtered_list)
        print("Unique Users:", unique_users)
        print("Frequency:", freq)
        print("Active Users:", active_users)

    def get_user_messages(self, username):
        self.username=username
        return self.conversations.get(username, [])

logs = "alice:hi bob:hello alice:how_are_you bob:good charlie:hey invalid bob: :test"
chat1=Chat_Agent(logs)
chat1.Chat_Application(logs)

print(" Alice Messages:", chat1.get_user_messages("alice"))
print("Bob Messages:", chat1.get_user_messages("bob"))

