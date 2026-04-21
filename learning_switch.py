from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# MAC address table
mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.dpid
    in_port = event.port

    if not packet.parsed:
        log.warning("Ignoring incomplete packet")
        return

    src = packet.src
    dst = packet.dst

    # Initialize switch table
    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    # Learn source MAC
    mac_to_port[dpid][src] = in_port

    log.info("Learned MAC %s on port %s (switch %s)", src, in_port, dpid)

    # Check if destination MAC is known
    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]
        log.info("Forwarding packet %s -> %s via port %s", src, dst, out_port)

        # Install flow rule
        msg = of.ofp_flow_mod()
        msg.match.dl_dst = dst
        msg.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(msg)

    else:
        out_port = of.OFPP_FLOOD
        log.info("Flooding packet %s -> %s", src, dst)

    # Send packet out
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    msg.in_port = in_port
    event.connection.send(msg)


def launch():
    log.info("Custom Learning Switch Controller Started")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)