<template>
  <div :class="['message-box', messageType]">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
export default class MessageBox extends Vue {
  @Prop() private messageType!: string
}
</script>

<style lang="scss" scoped>
.message-box {
  border: 2px solid;
  border-radius: 5px;
  font-weight: lighter;
  font-size: 18px;
  padding: 5px;
  margin: 10px;
}

.error {
  background-color: #aa2727b7;
  border-color: #f13434;
  color: #fff6f6;
}

.warning {
  background-color: #fff3cd;
  border-color: #ffeeba;
  color: #856404;
}

.info {
  background-color: #d1ecf1;
  border-color: #bee5eb;
  color: #0c5460;
}

.success {
  background-color: #d4edda;
  border-color: #c3e6cb;
  color: #155724;
}
</style>
