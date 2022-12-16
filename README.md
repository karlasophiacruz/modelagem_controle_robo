
## MODELAGEM E CONTROLE POR FORÇA PARTE 1

Repositório criado para o projeto Controle por força parte 1, da disciplina modelagem e controle de robôs do semestre 2022.1. O grupo é formado por Jonata Oliveira da Silva, Karla Sophia Santana Cruz, Lívia de Maria Calado Machado Soares, Lilian Giselly Pereira Santos, Pedro Henrique de Brito Nascimento, Rebeca de Jesus Brandão e Ullyanne Júlia Freire Patriota.

De acordo com as instruções, a atividade foi realizada no simulador coppelia e os algorítimos da força, modelagem dinâmica e da cinemática direta foram implementados em python. Os plots estão na pasta "Plot" e contém os gráficos de força.

###### Dentro do projeto foram atendidos os seguintes tópicos: 

1. Observe que rodar o solid_simple.ttt mantém o robô erguido, uma vez que o comando de posição implementa uma malha de controle interno em cada junta. Por outro lado, quando rodamos solid_force.ttt os elos do manipulador caem, já que não há nada compensando a gravidade.
2. Focando na solid_simple.ttt, implemente, com a API do Coppelia para ZeroMQ ou ROS (não será aceito o uso da API Remota clássica, pois já está com status deprecated), um script para pegar e plotar as forças de cada junta por um período de tempo.
3. Implemente um algoritmo para pegar essas forças do passo anterior e aplicar nas juntas do exemplo solid_force.ttt
4. Estabeleça o modelo dinâmico desse robô no espaço de juntas, relacionando os torques à aceleração das juntas
5. Traga esse modelo para o espaço de trabalho, relacionando a força exercida no efetuador à acelaração (ou torque) das juntas.
