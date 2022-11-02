class Star_Cinema:
	hall_list = []
	def __init__(self):
		pass
	def entry_hall(self,hall):
		self.hall_list.append(hall)

class Hall(Star_Cinema):
	def __init__(self, rows, cols, hall_no):
		self.__seats = {}
		self.__show_list = []
		self.rows = rows
		self.cols = cols
		self.hall_no = hall_no
		super().entry_hall(self)

	def entry_show(self, id, movie_name, time):
		self.__show_list.append((id, movie_name, time))
		arr = []
		for i in range(self.rows):
			col = []
			for j in range(self.cols):
				col.append(chr(65 + i) + str(j + 1))
			arr.append(col)
			dd = dict([(id, arr)])
			self.__seats.update(dd)

	def book_seats(self):

		customer_name = input('ENTER CUSTOMER NAME: ')
		phone_number = input('ENTER CUSTOMMER PHONE NUMBER: ')
		id = input('ENTER SHOW ID: ')
		flg = 0
		flg2 = 0
		flg3 = 0
		booked_seat = []
		seat_for_book = []
		already_booked = []
		not_found = []

		for ID in self.__seats.keys():
			
			if ID == id:
				tt = id = int(input('ENTER NUMBER OF TICKETS : '))
				for khuki in range(tt):
					st = input('ENTER SEAT NUMBER: ')
					st = (ord(st[0]) - 65, int(st[1]) - 1)
					seat_for_book.append(st)
				for k in seat_for_book:
					if k[0]<self.rows and k[1]<self.cols:
						if self.__seats[ID][k[0]][k[1]] != 'X':
							temp = self.__seats[ID][k[0]][k[1]]
							self.__seats[ID][k[0]][k[1]] = 'X'
							booked_seat.append(temp)
							flg = 1
						else:
							temp2 = self.__seats[ID][k[0]][k[1]]
							already_booked.append(temp2)
							flg2 = 1
					else:
						temp3 = chr(k[0]+65)+str(k[1]+1)
						not_found.append(temp3)
						flg3 = 1
			else:
				flg = 2
			
			if flg == 1:
				break

		if flg == 1:
			print('\n')
			print(f'##### TICKET BOOKED SUCCESSFULLY!! #####')
			print('======='*10)
			print(f'NAME: {customer_name}')
			print(f'PHONE NUMBER: {phone_number}')
			i = 0
			lenOFshow = self.__show_list.__len__()
			while(i < lenOFshow):
				for j in self.__show_list[i]:
					if j == ID:
						xx = self.__show_list[i].index(j)
						print(f'MOVIE NAME: {self.__show_list[i][xx+1]}        MOVIE TIME: {self.__show_list[i][xx+2]}')
				i += 1
			print('TICKETS: ', end=' ')
			for ticket in booked_seat:
				print(ticket, end=' ')
			print('\n')
			print(f'HALL: {self.hall_no}')
			print('======='*10)
		elif flg == 2:
			print('====='*5)
			print('ID DIDN', end="'")
			print("T MATCH WITH ANY SHOW!")
			print('====='*5)
		if flg2 == 1:
			print('========='*5)
			print('THESE SEATS WERE BOOKED -', end=' ')
			for ticket in already_booked:
				print(ticket, end=' ')
			print()
			print('========='*5)
		if flg3 == 1:
			print('========'*5)
			print('INVALID SEAT N0 -', end=' ')
			for ticket in not_found:
				print(ticket, end=' ')
			print()
			print('========'*5)

	def view_show_list(self):
		print('\n')
		print("----------"*10)
		print('\n')
		for show in self.__show_list:
			
			print(f'MOVIE NAME: {show[1]}\t\tSHOW ID: {show[0]}\t\tTIME: {show[2]}')
			print('\n')
		print('----------'*10)
	
	def view_available_seats(self):
		id = input('ENTER SHOW ID: ')
		flg = 0
		for i in range(self.__show_list.__len__()):
			for j in self.__show_list[i]:
				if j == id:
					flg = 1
					break
		if flg == 0:
			print('\n')
			print('======'*5)
			print('ID DIDN', end="'")
			print("T MATCH WITH ANY SHOW!")
			print('======'*5)
		else:
			for i in range(self.__show_list.__len__()):
				for j in self.__show_list[i]:
					if j == id:
						xx = self.__show_list[i].index(j)
						print('\n')
						print(
							f'MOVIE NAME: {self.__show_list[i][xx+1]}\tTIME: {self.__show_list[i][xx+2]}')
			print('X for allready booked seats')
			print()
			print('======'*10)
			for(i, j) in enumerate(self.__seats[id]): 
				for k in j:
					if k != 'X':
						print(k, end='           ')
					else:
						print('X', end='           ')
				print()
			print('======'*10)

# int main()
hall1 = Hall(5, 5, 'H-11')
hall1.entry_show('dc17', 'Justice League', 'Nov 22 2022 11 AM')
hall1.entry_show('dc08', 'The Dark Knight', 'Nov 22 2022 4 PM')

#  take user input
while True:
	print('\n')
	print('1. VIEW ALL SHOWS TODAY')
	print('2. VIEW AVALIABLE SEATS')
	print('3. BOOK SEATS')
	print('\n')
	choice = input('ENTER OPTION: ')
	
	if choice == '1':
		hall1.view_show_list()
	elif choice == '2':	
		hall1.view_available_seats()
	elif choice == '3':
		hall1.book_seats()
	else:
		print('WRONG OPTION TRY AGAIN')