# O Problema do Produtor-Consumidor

O problema do produtor-consumidor é um exemplo clássico de sincronização em sistemas operacionais e programação concorrente. Ele ilustra a comunicação entre threads ou processos que compartilham um buffer de tamanho limitado.

## Descrição do Problema

- **Produtor**: Gera dados e os armazena em um buffer compartilhado
- **Consumidor**: Remove e processa os dados do buffer compartilhado
- **Buffer**: Área de memória compartilhada com tamanho limitado

## Desafios

1. **Sincronização**: Garantir acesso seguro ao buffer compartilhado
2. **Condições de Corrida**: Evitar que produtores e consumidores acessem o buffer simultaneamente
3. **Deadlocks**: Prevenir situações onde processos ficam bloqueados indefinidamente

## Condições a Serem Garantidas

- Produtor não pode adicionar dados quando o buffer estiver cheio
- Consumidor não pode remover dados quando o buffer estiver vazio
- Múltiplos produtores/consumidores não podem acessar o buffer ao mesmo tempo

Este problema é fundamental para entender conceitos de:
- Exclusão mútua
- Sincronização de threads
- Comunicação entre processos