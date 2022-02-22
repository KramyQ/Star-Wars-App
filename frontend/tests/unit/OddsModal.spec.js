import oddsModal from "@/components/oddsPrediction/oddsModal.vue";
import { mount } from "@vue/test-utils";

jest.mock("@/services/OddPredictionService")


describe("oddsModal.vue", () => {
  it("Modal shows emits close event on button clicked", () => {
    const wrapper = mount(oddsModal)
    wrapper.find('button').trigger('click')
    const closeModalCall = wrapper.emitted('close-modal')
    expect(closeModalCall).toHaveLength(1)
  })

  it("Modal binded props gets rendered", () => {
    const wrapper = mount(oddsModal, {props: {message: 'test'}})
    expect(wrapper.find('#message-display').text()).toBe('test')
  })
})
