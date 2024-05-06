library(MASS)
install.packages("read")

setwd("C:\\Users\\user\\Desktop\\영주시데이터")
list.files()
# 원본 데이터
original_data <- read.csv("면적당데이터.csv", fileEncoding = "CP949")
original_data <- original_data[,-c(1)] # 지역이름 제거
original_data # 확인

# 평균과 표준편차 계산
mean_values <- colMeans(original_data)
sd_values <- apply(original_data, 2, sd)

# 평균과 표준편차를 기준으로 정규분포를 따르는 모의 데이터 생성
simulated_data <- mvrnorm(n = 21, mu = mean_values, Sigma = diag(sd_values))

# 결과 확인
simulated_data

write.csv(simulated_data, file = "simulated_data2.csv", row.names = FALSE)
