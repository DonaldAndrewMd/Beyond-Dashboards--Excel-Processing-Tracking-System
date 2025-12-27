# excel-order-management-sample
Fictional hospital-pharmacy order tracker showing how Excel can automate workflows and track orders like a lightweight program

## **Background**

### **Client:**
Forsythe Pharmacy (Fictional Retailer) 

### **Location:** 
Abuja 

### **Service Model:** 
Just-in-Time (JIT) Medication Delivery

### **Client Story:**
Forsythe pharmacy enables partner hospitals to operate without holding their own expensive stock. Instead, they offer an "as-required" ordering system. When a hospital needs a specific drug for a patient, Forsythe fulfills and dispatches it immediately promising delivery within minutes to a few hours, depending on proximity.
While the logistics were innovative, the communication layer was primitive. At the time of engagement, the entire operation relied on WhatsApp.
Every partner hospital had a dedicated group chat.
Hospital reps manually typed out patient-specific orders.


#### **Existing Workflow (Before)**

Before any form of intervention, Forsythe Pharmacy’s order management process was entirely manual and chat-driven.

1. Partner hospital staff send patient prescriptions as text or photos via dedicated WhatsApp group chats
2. Forsythe staff manually monitor and read incoming messages
3. Inventory availability is checked manually, after which drug names and prices are typed out by hand as a confirmation of availability to the partner.
5. Fulfilled orders are replied to directly within the same hospital chat
6. Once delivery is completed, fulfillment updates are communicated back through chat
7. No structured or centralized record of orders is maintained
8. In the event of disputes, message order and timestamps are manually reviewed to verify claims

While functional at a small scale, this workflow depended heavily on human memory, attention, and constant vigilance.


#### **Core Challenges Identified**
**1. Message Overload & Operational Noise**
- Forsythe works with over 21 partner hospitals, with each staff member handling requests from approximately three hospitals
- Multiple hospitals send requests simultaneously
- Non-operational messages (greetings, acknowledgements, clarifications, confirmations) flood the same channel
- Critical prescriptions and instructions are quickly buried
- High risk of legitimate requests being missed or delayed

This created an environment where important operational signals were lost in conversational noise.

**2. Duplicate & Overlapping Requests**
- Multiple staff members from the same hospital often send the same prescription
- No deduplication or request validation mechanism exists
- This leads to:
* Duplicate processing
* Confusion around fulfillment status
* Repeated inventory checks
* Unnecessary operational friction

**3. Missed or Forgotten Requests**
- No defined states such as Pending, In Progress, or Completed
- Order tracking relies entirely on human memory
- If a staff member steps away or gets overwhelmed, requests can be forgotten entirely

**4. No Ownership or Accountability**
- Requests are not assigned to specific Hospital staff
- No visibility into:
* Who is handling which order
* What is delayed
* What is stuck or abandoned
As a result, responsibility is diffused and follow-ups are reactive rather than proactive.

**5. Data Loss Risk**
-WhatsApp serves as the only “database”
- Risks include:
 * App crashes
 * Device loss
 * Accidental deletion
 * Any of these results in permanent data loss
 * No backups
 * No audit trail

**6. Zero Reporting & Analytics**
- WhatsApp messages are:
  * Unstructured
  * Non-tabular
  * Difficult to query or analyze
-As a result, Forsythe lacks:
* Daily or weekly order counts
* Hospital-level demand analysis
* Drug-level frequency tracking
* Turnaround time metrics
* Evidence-based operational insights
* Decision-making is largely driven by intuition.

**7. Poor Interoperability**
- Data cannot be easily exported into Excel or reporting tools
- Management cannot quickly answer basic operational questions like:
* “Which hospital requests the most medications?”
* “Which drugs are frequently delayed?”
* “Where are our bottlenecks?”

**8. Scalability Limitations**
-As the number of partner hospitals grows:
* Chat volume increases exponentially
* Error rates increase
* Reliability decreases
- WhatsApp does not scale as an operational system.

**9. Compliance & Audit Concerns**
- No structured patient request log
- No timestamped fulfillment history
- Auditing past transactions is difficult and unreliable
- Regulatory review is time-consuming

**10. Staff Fatigue & Burnout**
- Continuous monitoring of multiple chat groups
- High cognitive load from manual tracking
- Stress driven by fear of missing urgent patient requests

The system puts the operational burden on the people rather than on the processes.


### Summary:
Forsythe Pharmacy use WhatsApp to manage just-in-time drug orders from hospitals. When the number of hospitals grew, this caused missed and duplicate orders, poor accountability,, no reporting, and a system that was unreliable and hard to audit for pharmacy operations.
