<template>
  <div
    id="color-circl-team-name"
    :style="{ 'justify-content': justifyContent, }">
    <ColorCircle :teamColorHex="team.colour"/>
    <span>
      {{ team.teamName }}
    </span>
  </div>
</template>

<script>
import ColorCircle from '@/components/ColorCircle.vue';

export default {
  name: 'ColorCircleTeamName',
  props: {
    team: Object,
    justifyContent: String,
  },
  components: {
    ColorCircle,
  },
};
</script>

<style scoped lang="scss">
#color-circl-team-name{
  display: flex;
  align-items: center;
}
</style>
