x=int(input("Enter an amount of time (in seconds): "));
hours = (x//3600);
minutes = (x%3600)//60;
seconds = (x%60)
print(f"{x} seconds is {hours} hours, {minutes} minutes and {seconds} seconds.");
