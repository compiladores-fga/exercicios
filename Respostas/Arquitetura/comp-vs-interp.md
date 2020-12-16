### Q1
Compiladores fazem a tradução de um código-fonte inteiro para um código de máquina que pode ser interpretado pelo computador. Caso haja modificações nesse código-fonte, ele precisa ser recompilado.
Já os interpretadores traduzem o código-fonte linha a linha, por isso se houverem mudanças no código, nem sempre é preciso interpretá-lo do zero.
Compiladores tendem a ser mais rápidos e mais confiáveis que interpretadores pois possuem diversas etapas de validação, porém uma vantagem dos interpretadores é a independência de plataformas (Windows, Linux, etc) por rodarem em tempo de execução.

### Q2
Uma implementação "compilada" do Python é o PyPy. Através da compilação Just-In-Time(JIT), o PyPy identifica bytecodes que são executados frequentemente e os compila para código de máquina nativo, que são mais rápidos. Ou seja, essa é uma técnica híbrida que mistura as vantagens de compiladores e interpretadores.