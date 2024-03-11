h=float(input('請輸入身高(公分)'))/100
w=float(input('請輸入體重(公斤)'))
print('您輸入的身高為：', h*100, '公分')
print('您輸入的體重為：', w, '公斤')
bmi=round(w/(h*h),2)
print('您的BMI數值為：', bmi)
