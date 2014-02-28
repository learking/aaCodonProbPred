#read in csv and set column names for it
library(data.table)
data = fread('/home/kuangyu/workspace/aaCodonProbPred/studyHydroResult/aaProb_sa_0_172.csv')
setnames(data, c('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'))

x = seq(1,172,2)

for(i in names(data)){
	tmpFname = paste0("/home/kuangyu/workspace/aaCodonProbPred/studyHydroResult/fig/",i,"_sanac.png")
	png(filename=tmpFname)
	plot(x,data[,get(i)],xlab=i)
	dev.off()
}
