class Store_In_DB():
	def __init__(self, password,  hot_name, verify, file_path, verification_password, cnt_lines):
		self.password = password
		self.hot_name = hot_name

		self.verify = verify
		self.verification_password = verification_password

		self.file_path = file_path 
		self.cnt_lines = cnt_lines

	def djb2(self, string_text):
		sum = 0
		modulo_number = 997

		for char in string_text:
			sum += ord(char)

		return sum % modulo_number

	def prepare_file(self):
		file = open(self.file_path, "a")

		for line in range(1000):
			file.writelines("_\n")

	def Write_text(self):
		file = open(self.file_path, "r")

		#Text to that will be stored in our DB
		text_list = [self.hot_name, self.password, "\n"]
		string_text = ':'.join([str(elem) for elem in text_list])

		index_to_add = Store_In_DB.djb2(self, self.hot_name)

		all_lines = file.readlines()
		all_lines[index_to_add] = string_text
		file.close()

		file = open(self.file_path, "w")
		file.writelines(all_lines)
		file.close()


		self.cnt_lines += 1

	def Delete_text(self):
		file = open(self.file_path, "r")

		index_to_remove = Store_In_DB.djb2(self, self.hot_name)

		all_lines = file.readlines()
		all_lines[index_to_remove] = "_\n"
		file.close()

		file = open(self.file_path, "w")
		file.writelines(all_lines)
		file.close()


		self.cnt_lines += 1

	def Get_Password(self):
		file = open(self.file_path, "r")

		try:
			index_of_hotname = Store_In_DB.djb2(self, self.hot_name)
			password_username = file.readlines()[index_of_hotname]

			password = ""
			start_extracting = False

			for cur_char in password_username:
				if cur_char == ":" and start_extracting == False:
    					start_extracting = True

				if cur_char != ":" and start_extracting == True:
    					password += cur_char

			print(f"The password of your {self.hot_name} account is {password}")
		except:
			print("Could not find your hot_name")
				

DB_Manager = Store_In_DB("123", "a", False, "DATA_BASE.txt", "verification password", 0)
DB_Manager.Get_Password()
