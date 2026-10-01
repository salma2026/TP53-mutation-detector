# TP53 mutation detector
#### Video Demo:  <https://youtu.be/LrMceXn1iZQ>
#### Description:
This project is a TP53 mutation detector where i have a reference healthy DNA sequence file (fasta file) and teh program expcets the user to input a fasta file or txt file to analyze it and detects the different nucleotides and amino acids and outputs a report containing:
* the number of base pairs
* codons, number of different nucleotides
* number of different amino acids
* the original codon and mutated one
* the original amino acid and mutated one
* the index of mutated nucleotide
* the index of mutated amino acid
* the time and date when this program is executed
Additionally, the user can install that report if they wanted as txt file. More on the program itself it is made of multiple functions and this is because i wanted to break down each task into a function so i dont have mixed concerns.therefore i made each function handle a task.

- First function, opens the fasta or txt file , read it , remove any unwanted spaces , ignore the fasta header line and return a string with the clean dna
- Second function, checks whether this is a TP53 gene DNA or not also checks the inputted file extension returning a boolean.
- Third function,split dna into codons so they are easier to compare later returing a list of codons.
- Fourth function, it takes 2 parameters (the healthy DNA and inputted DNA) looping through the list of codons of the inputted DNA and comparing it to the list of codons of the healthy one returning a list of the original codon , mutated(different) codon and index, this function is versatile as i used for the comparison between the nucleotides and betweeen the translated amino acids.
- Fifth function,from the biopython library i did import translate function it translates the sequence of DNA into amino acids.
- Sixth function, it was mainly for collection of data in one place so i can display it for the user using another function so, it collects the data and put it into a dictionary then pass it to .items() function that change it into dict_items so, they can be iterated through and used in tabulate function later which needs a list of lists.
- Seventh function, this is one is the report generator which dispalys a table cotaining all the data in the sixth function.
- The eighth function which asks the user if they want to download the report as a txt file if yes it asks the user for the desired name for the file and download , if no it just exits.

Also , my code does deal with unwanted file extensions , healthy inputted dna that contains no mutations, as well as any wrong inputs. In requirments.txt , it has all the installed libraries used in my code.In test_project , it has 3 functions for testing the function imbeded in my project file.And lastly there are multiple TP53 files for testing the program.
