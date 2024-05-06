library(car) # vif()
getwd()
setwd("C:\\Users\\hj123\\OneDrive\\바탕 화면")

data <- read.csv("영주싀.csv", fileEncoding = "CP949")
str(data)

yeongju <- data[ ,-c(1,2,3)] # 필요없는 col 제거
str(yeongju)

for (i in 1:ncol(yeongju)) { # integer -> numeric 변환
  if (is.integer(yeongju[[i]])) {
    yeongju[[i]] <- as.numeric(yeongju[[i]])
  }
}
str(yeongju)

# 다중회귀분석
lm_result <- lm(`청년.인구수` ~ `평당.평균.전세` + `레저시설.수` + `보육시설.수` + `교육시설.수` + `정류장.수` + `청년경제지수`, data = yeongju)

summary(lm_result)
vif(lm_result) # 10이상이면 다중공선성 높음;;

fitted_values <- predict(lm_result) # 종속변수의 예측값을 계산

plot(yeongju$`청년.인구수`, fitted_values, 
     xlab = "관측된 청년 인구수", ylab = "피팅된 청년 인구수",
     main = "관측값 vs 피팅된값",
     col = "blue", pch = 16)


summary(lm_result)
vif(lm_result) # 10이상이면 다중공선성 높음;;
