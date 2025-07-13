Sub 教育数据质量检测()

    Dim lastRow As Long
    Dim i As Long
    Dim 学号 As String
    Dim 学习时长 As Double
    Dim 学习时间 As Date
    Dim 学习状态 As String
    Dim 完成状态 As String
    Dim 重复学号字典 As Object

    Set 重复学号字典 = CreateObject("Scripting.Dictionary")

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    Cells(1, 8).Value = "检测结果"

    For i = 2 To lastRow
        Dim 检测结果 As String
        检测结果 = ""

        学号 = Trim(Cells(i, 1).Value)
        学习时间 = Cells(i, 4).Value
        学习时长 = Cells(i, 5).Value
        学习状态 = Trim(Cells(i, 6).Value)
        完成状态 = Trim(Cells(i, 7).Value)

        If 重复学号字典.exists(学号) Then
            检测结果 = 检测结果 & "学号重复；"
        Else
            If 学号 <> "" Then
                重复学号字典.Add 学号, 1
            End If
        End If

        If 学习时长 < 30 Or 学习时长 > 80 Then
            检测结果 = 检测结果 & "学习时长异常；"
        End If

        If Hour(学习时间) >= 0 And Hour(学习时间) < 5 Then
            检测结果 = 检测结果 & "凌晨学习；"
        End If

        If 完成状态 = "" Or 完成状态 = "未完成" Then
            检测结果 = 检测结果 & "未完成；"
        End If

        If 学习状态 = "正常" And 完成状态 = "未完成" Then
            检测结果 = 检测结果 & "状态逻辑冲突；"
        End If

        If 检测结果 = "" Then
            检测结果 = "正常"
        End If

        Cells(i, 8).Value = 检测结果
    Next i

    MsgBox "检测完成，共检测 " & lastRow - 1 & " 条记录。", vbInformation

End Sub
