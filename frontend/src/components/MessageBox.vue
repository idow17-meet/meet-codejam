<template>
  <div class="message-box" :style="typeMapping[messageType]">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
export default class MessageBox extends Vue {
  @Prop() private messageType!: string

  private typeMapping: any = {
    error: {
      backgroundColor: '#fdcdcd',
      borderColor: '#f13434',
      color: '#ff4747',
    },
    warning: {
      backgroundColor: '#fff3cd',
      borderColor: '#ffeeba',
      color: '#856404',
    },
    info: {
      backgroundColor: '#d1ecf1',
      borderColor: '#bee5eb',
      color: '#0c5460',
    },
    success: {
      backgroundColor: '#d4edda',
      borderColor: '#c3e6cb',
      color: '#155724',
    },
  }
}
</script>

<style lang="scss" scoped>
.message-box {
  border: 1px solid;
  border-radius: 5px;
  font-weight: lighter;
  font-size: 18px;
  padding: 5px;
}
</style>
