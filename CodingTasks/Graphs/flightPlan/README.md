Note: Try to solve this task in O(m log n) time, where n is a number of cities and m is a number of flights, since this is what you'll be asked to do during an interview.

Elle is trying to arrange a flight from source to dest. She doesn't mind taking multiple connecting flights, but wants to get to her destination dest as soon as possible. She has a timetable of flights, times, where:

times[i][0] is the starting location of flight i,
times[i][1] is the destination for flight i,
times[i][2] is the time flight i departs,
times[i][3] is the time flight i arrives.
The earliest Elle can leave is midnight (00:00). All times have been encoded as HH:MM. All times are referenced in the timezone of the source, where the hours HH are bigger than 23 if the time is on a subsequent day.

Given the timetable times, source, and dest, return the time when Elle will arrive at dest, if she wants to get here as soon as possible, or "-1" if it's impossible. For her flights:

Assume they all leave and arrive on time.
She needs 60 minutes between flights.
