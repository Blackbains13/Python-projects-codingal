function palindrome(mystring){
    // incase if any special characters or spaces are given in input that has to be removed
    var input = mystring.replace(/[^A-Z0-9]/ig, "").toLowerCase();
    
    // to check palindrome or not the string needs to be reveresed so we are reversing it by splitting and joining it
    var reverseInput = input.split('').reverse().join('');
    
    // checking for palindrome
    if (input === reverseInput){
      document.write("<div>" + mystring + " is a palindrome <div>")
    }
    else{
      document.write("<div>" + mystring + " is not a palindrome <div>")
    }
  }
  
  // invoking function
  palindrome("Civic")