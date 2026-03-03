Ran on server csx3

	ssh onto csx
	in the terminal enter
	gcc assignment02_webb_eli.c -o question02
	then ran with
	./question02

ewebb11@csx3:~$ nano assignment02_webb_eli.c
ewebb11@csx3:~$ gcc assignment02_webb_eli.c -o assignment02
ewebb11@csx3:~$ ./assignment02
[Frontend] @ 42s: Sending Alice...
[Database] @ 42s: Start processing Alice...
[Frontend] @ 43s: Sending Bob...
[Frontend] @ 44s: Sending Charlie...
[Frontend] @ 45s: All students submitted! My job is done.
[Database] @ 45s: Finished processing Alice. Assigned ID: 1001
[Database] @ 45s: Start processing Bob...
[Logger] @ 45s: CONFIRMED - ID: 1001, Name: Alice
[Database] @ 48s: Finished processing Bob. Assigned ID: 1002
[Logger] @ 48s: CONFIRMED - ID: 1002, Name: Bob
[Database] @ 48s: Start processing Charlie...
[Database] @ 51s: Finished processing Charlie. Assigned ID: 1003
[Logger] @ 51s: CONFIRMED - ID: 1003, Name: Charlie
[Parent] All processes finished. Queue destroyed.