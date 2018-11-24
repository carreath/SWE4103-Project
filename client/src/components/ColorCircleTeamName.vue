<template>
  <div id="color-circl-team-name">
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
  },
  components: {
    ColorCircle,
  },
};
</script>

<style scoped lang="scss">
#color-circl-team-name{
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
