# a script to analyze the diversity between 17 microbial genomes of the order Vibrionales

#work directory
setwd("~/Dropbox/Cod_microbiome/phylogeny/jSpeciesW_results/input_genomes/")


#Loading libraries
library(ggplot2)
library ("grid")
library("gridExtra")
library("cowplot")




#Loading datasets
mash_results <- read.delim("vibrionales_mash_results_edit.txt", header=FALSE)
colnames(mash_results) <- c("Genome_A", "Genome_B","Mash_distance", "P-value", "Matching Hashes")

fastANI_results <- read.delim("fastANI_results.ANI_edit.txt", header=FALSE)
colnames(fastANI_results) <- c("Genome_A", "Genome_B","ANI_value", "bidirectional fragment mappings (n)", "total query fragments")

#converting mash distances, to inverse distances
mash_results$Inv_MASH <- 1-mash_results$Mash_distance

#calculating alignment fraction
fastANI_results$Alignment_fraction <- round((fastANI_results$`bidirectional fragment mappings (n)`/fastANI_results$`total query fragments`), digits=3)


#plotting the mash results heatmap
# colors(white - steelblue)

(mash_plot <- ggplot(mash_results, aes(Genome_A, Genome_B )) +
  geom_tile(aes(fill =Inv_MASH), color = "white") +
  scale_fill_gradient(low ="white", high = "steelblue") +
  ylab("") +
  xlab("") +
  theme(legend.title = element_text(size = 10),
        legend.text = element_text(size = 12),
        plot.title = element_text(size=16),
        axis.title=element_text(size=14,face="bold"),
        axis.text.x = element_text(angle = 90, hjust = 1)) +
  labs(fill = "Mash distance"))

Save plot as eps size 1000 and 1000. 
#plotting the ANI similarity heatmap
# colors(white - steelblue)

(ani_plot <- ggplot(fastANI_results, aes(Genome_A, Genome_B )) +
  geom_tile(aes(fill = ANI_value), color = "white") +
  scale_fill_gradient(low = "white", high = "steelblue") +
  ylab("") +
  xlab("") +
  theme(legend.title = element_text(size = 10),
        legend.text = element_text(size = 12),
        plot.title = element_text(size=16),
        axis.title=element_text(size=14,face="bold"),
        axis.text.x = element_text(angle = 90, hjust = 1)) +
  labs(fill = "ANI (%)"))

Save plot as eps size 1000 and 1000.
#plotting the Aligned fraction heatmap
# colors(white - steelblue)

(align_plot <- ggplot(fastANI_results, aes(Genome_A, Genome_B )) +
    geom_tile(aes(fill = Alignment_fraction ), color = "white") +
    scale_fill_gradient(low = "white", high = "steelblue") +
    ylab("") +
    xlab("") +
    theme(legend.title = element_text(size = 10),
          legend.text = element_text(size = 12),
          plot.title = element_text(size=16),
          axis.title=element_text(size=14,face="bold"),
          axis.text.x = element_text(angle = 90, hjust = 1)) +
    labs(fill = "Alignment fraction")+
    geom_text(aes(Genome_A, Genome_B, label = Alignment_fraction), color = "black", size = 4))
Save plot as eps size 1000 and 1000.


# Plot the grid and add A, B labels:
plot_grid(mash_plot, ani_plot, align_plot, labels = c("A", "B", "C"), ncol = 2, nrow = 2 )



# Save plot as eps size 850 and 1100. 

