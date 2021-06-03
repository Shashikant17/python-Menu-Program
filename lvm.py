import os
def lvmconf():
	os.system("tput setaf 2")
	print("\t\t----------------------------------------")
	print("\t\t\t\tAVAILABLE MENUS")
	print("\t\t-----------------------------------------")
	os.system("tput setaf 7")
	print("\t\t\t1. Check available disks")
	print("\t\t\t2. Create physical volumes(PV)")
	print("\t\t\t3. Create Volume Group (VG)")
	print("\t\t\t4. Create Logical volumes(LV)")
	print("\t\t\t5. Format the created LV")
	print("\t\t\t6. Mount the LV")
	print("\t\t\t7. Extend Volume Group")
	print("\t\t\t8. Format the extende volume")
	print("\t\t\t9. To display volume group.")
	print("\t\t\t0. to display Logical volume.")
	
	os.system("tput setaf 7")
	lvm = int(input("Enter your choice : "))
	if lvm == 1:
		p = os.system('fdisk -l')
		print(p)
	elif lvm == 2:
		y = int(input("How many hard disks do you want to convert into PV:"))
		for i in range(y):
			r = str(i+1)
			p = input("Enter the name of disk no "+r+" :")
			q = os.system("pvcreate {0}".format(p))
			print(q)
			input()
	elif lvm == 3:
		a = input("Enter the name for volume group which is to be created :")
		b = input("Enter name of physical volume (please separate the names by giving space if you want to give more than one):")
		s = os.system("vgcreate {0} {1} ".format(a,b))

	elif lvm == 4:
		e = input("Enter size for LV in (G/M/T):")
		d = input("Enter name for LV :")
		f = input("Enter name of created volume group: ")
		lv = os.system("lvcreate --size {0} --name {1} {2}".format(e,d,f))
	elif lvm == 5:
		vg_nm = input("Enter Created VG name :")
		lv_nm = input("Enter Created LV name :")
		frmt = os.system("mkfs.ext4 /dev/{0}/{1}".format(vg_nm,lv_nm))
	elif lvm == 6:
		vg = input("Enter created name of volume group.")
		ln = input("Enter Created LV name :")
		dr = input("Enter name to create directory:")
		os.system("mkdir /{0}".format(dr))	
		print("mounting your partition on created directory...")
		os.system("mount /dev/{0}/{1} /{2}".format(vg,ln,dr))
		print("partition mounted successfully")
		input()
	elif lvm == 7:
		u = input("Howm much size do you want to extend ,Enter size in (G/M/T):")
		w = input("Enter name of created volume group: ")
		v = input("Enter name of created LV :")
		resize = os.system("lvextend --size +{0}  /dev/{1}/{2}".format(u,w,v))
		print(resize)
		input()
	elif lvm == 8:
		r_v = input("Enter name of created volume group: ")
		r_l = input("Enter name of created LV :")
		re_frmt = os.system("resize2fs /dev/{0}/{1}".format(r_v,r_l))
		print(re_frmt)
		input()
	elif lvm == 9:
		vgname=input("enter vg name:")
		v_disp = os.system("vgdisplay {0}".format(vgname))
		print(v_disp)
		input()
	elif lvm == 0:
		vgname2=input("Enter vg name:")
		lvname=input("Enter lv name:")
		lv_display=os.system("lvdisplay {}/{}".format(vgname2,lvname))
		print(lv_display)
		input()
	else:
		print("invalid input chech once again.")
		input()

def lvmrepeat():
    lvmconf()
    a=input("Wish to continue?(y/n)")
    if a == 'y' :
        lvmconf()
    elif a == 'n':
        os.system("exit")
    else:
        print("Kindly check your input")
        
lvmrepeat()
