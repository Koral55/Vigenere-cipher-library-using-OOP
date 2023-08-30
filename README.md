# HOW TO USE
1. To **receive a coded message** you can assign it to a variable like so: coded_message = Vigenere.code(text="example text", key="examplekey")
2. To **receive a decoded message** you can assign it to a variable like so: decoded_message = Vigenere.decode(code="example coded message", key="examplekey")
3. Your **message** can only contain **lowercase letters** and **spaces**
4. Your **key** can only contain **lowercase letters**
5. Your **key length** can be either **shorter**, **same length**, or **longer** than the message
