Attribute VB_Name = "Module1"
Function RemoveSpecChar(sInput As String) As String
    Dim sSpecChar As String
    Dim i As Long
    sSpecChar = "\/:*?™""®<>|.&@#(_+`©~);-+=^$!'"
    For i = 1 To Len(sSpecChar)
        sInput = Replace$(sInput, Mid$(sSpecChar, i, 1), "")
    Next
    RemoveSpecChar = sInput
End Function
